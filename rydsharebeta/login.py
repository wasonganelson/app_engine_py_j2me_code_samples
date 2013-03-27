from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.api import images
from database import * #need this module to access datastore ...
import time #need this for timestamping ...

class Login(webapp.RequestHandler):
   def get(self):
      #check if user session is valid before proceeding ...
      user = users.get_current_user()
      if not user:
         self.redirect(users.create_login_url(self.request.uri))
      else:
         header = '''<!doctype html> 
<html>
	<head>
		<meta name="HandheldFriendly" content="true" />
		<meta name="viewport" content="width=device-width; initial-scale=1.0; minimum-scale=1.0; maximum-scale=1.0;" />
		<meta name="apple-mobile-web-app-capable" content="yes" />
		<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
		<link type="text/css" rel="stylesheet" href="jscss/jqmcss.css" />
		<link type="text/css" rel="stylesheet" href="jscss/style.css" />
		<script type="text/javascript" src="jscss/jqjs.js"></script>
                <script type="text/javascript" src="jscss/custom.js"></script> 
		<script type="text/javascript" src="jscss/jqmjs.js"></script> 
                <title> 
			Rideshare-Ke
		</title> 
	</head> 
	<body>
		<div data-role="page"> 
			<div data-role="header" data-theme="a">
				<h3>Rideshare-Ke</h3>
			</div>'''
         content = '''
<div data-role="content" data-theme="a">
            <div class="signupcontent">
              <img class="ridesharekenyaprofileimage" alt="upload image" src="/images/logo.jpg"/><br/><br/>
              <div class="ridesharekenyaprofiletext">
                 <b>email:</b> %s<br/>
              </div>
              <form method="post" action="/login" enctype="multipart/form-data">
                <br/>
                to proceed, please upload a profile image and fill all details required below<br/><br/><b>profile image:</b><br/><input type="file" name="image" id="image" />
                <br/>
                <label for="username"><b>username:</b></label>
                <input type="text" name="username" id="username" value=""/><br/>
                <label for="userphonenumber"><b>tel no:</b></label>
                <input type="text" name="userphonenumber" id="userphonenumber" value="+254" /><br/>
                <label for="userpreferences"><b>user preferences:</b></label>
                <textarea name="userpreferences" id="userpreferences" onclick=this.value="">-no pets in my car\n-no smoking ...</textarea><br/>
                <input class="button" type="submit" value="upload"/><br/><br/>
              </form>
            </div>
        </div>''' % (users.get_current_user().email())
         footer = '''<div data-role="footer" data-theme="a"> 
			<h6 class="footertext">&copy Rideshare-Ke</h6>
		</div>
</body>
</html>'''
         #check that user is signed up ...
         useremail = user.email()
         query= Userstable.all()
         query.filter('useremail',useremail)
         queryresults = query.fetch(1,0)
         if queryresults:#if signed up, login user ...
            self.redirect("/ridesharekenyalogin")
         else:
            self.response.out.write(header+content+footer)

   def post(self):
      #check if user session is valid before proceeding ...
      user = users.get_current_user()
      if not user:
         self.redirect(users.create_login_url(self.request.uri))
      #check that user is signed up ...
      useremail = user.email()
      query= Userstable.all()
      query.filter('useremail',useremail)
      queryresults = query.fetch(1,0)
      if queryresults:#if signed up, login user ...
         self.redirect("/ridesharekenyalogin")
      else:
         primaryid = 0
         #get last primaryid ...
         query = Userstable.all()
         query.order('-timestamp') #order by timestamp desc ... most recent to least recent ...
         queryresults = query.fetch(1,0)
         if not queryresults:
            primaryid = 1
         else:
            for user in queryresults:
               primaryid = user.aaprimaryid + 1
         #upload user profile image ...
         try:
            image = images.resize(self.request.get('image'),200,200)
         except:
            image = ''
         if image == '':
            self.redirect('/login')
         else:
            newuser = Userstable()
            newuser.aaprimaryid = primaryid
            newuser.useremail = users.get_current_user().email()
            newuser.username = self.request.get('username')
            newuser.userphonenumber = self.request.get('userphonenumber')
            newuser.userpreferences = self.request.get('userpreferences')
            newuser.userprofileimage = db.Blob(image)
            newuser.timestamp = int(time.time())
            newuser.put()
            #update usernetwork table ...
            newuser = Usersnetworktable()
            newuser.aaprimaryid = primaryid
            newuser.useremail = users.get_current_user().email()
            newuser.usernetwork = ' '
            newuser.usernetworkrq = ' '
            newuser.put()
            self.redirect('/ridesharekenyalogin')
#end class Login ...
