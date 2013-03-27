from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.api import images
from database import * #need this module to access datastore ...

class Myaccount(webapp.RequestHandler):
   def get(self):
      #check if user session is valid before proceeding ...
      imagekey = ''
      useremail = ''
      username = ''
      userphonenumber = ''
      userpreference = ''
      user = users.get_current_user()
      if not user:
         self.redirect(users.create_login_url(self.request.uri))
      else:
         useremail = users.get_current_user().email()
         query = Userstable.all()
         query.filter('useremail',useremail)
         queryresults = query.fetch(1,0)
         for userdetails in queryresults:
            imagekey = userdetails.key()
            username = userdetails.username
            userpreferences = userdetails.userpreferences
            userphonenumber = userdetails.userphonenumber
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
		<div data-role="page" data-theme="a"> 
			<div data-role="header" data-theme="a">
				<h3>Rideshare-Ke</h3>
			</div>'''
      content = '''
<div data-role="content" data-theme="a">
            <div class="signupcontent">
              <img class="ridesharekenyaprofileimage" alt="upload image" src="/getimage?key=%s"/><br/><br/>
              <div class="ridesharekenyaprofiletext">
                 <b>email:</b> %s<br/>
              </div>
              <form method="post" action="/myaccount" enctype="multipart/form-data">
                <br/>
                update your details where necessary<br/><br/><b>new profile image:</b><br/><input type="file" name="image" id="image" />
                <br/>
                <label for="username"><b>new username:</b></label>
                <input type="text" name="username" id="username" value="%s"/><br/>
                <label for="userphonenumber"><b>new tel no:</b></label>
                <input type="text" name="userphonenumber" id="userphonenumber" value="%s" /><br/>
                <label for="userpreferences"><b>user preferences:</b></label>
                <textarea name="userpreferences" id="userpreferences" >%s</textarea><br/>
                <input class="button" type="submit" value="update"/><br/><br/>
              </form>
            </div>
        </div>''' % (imagekey, useremail, username, userphonenumber, userpreferences)

      footer = '''
<ul data-role="listview" data-inset="false" data-theme="a"> 
	<li>
		<a onclick="url='/ridessharedaroundme';getridessharedaroundme();"> 
			rides shared
		</a> 
	</li>
        <li> 
		<a onclick="url='/liftseekersaroundme';getliftseekersaroundme();"> 
			lift seekers
		</a> 
	</li>
        <li> 
		<a href="/postridelogin"> 
			share ride
		</a> 
	</li>
        <li> 
		<a href="/seekliftlogin"> 
			seek lift
		</a> 
	</li>
        <li> 
		<a href="/aboutlogin"> 
			about
		</a> 
	</li>
        <li> 
		<a href="/helplogin"> 
			help
		</a> 
	</li>
        <li> 
		<a href="/logout"> 
			log out
		</a> 
	</li>
</ul>
<div data-role="navbar" data-theme="a">
	<ul><li><a href="/ridesharekenyalogin">main<br/>menu</a></li>
	<li><a href="/myaccount">my<br/>account</a></li>
	<li><a href="/mynetwork">my<br/>network</a></li>
	<li><a href="/addtonetwork">add to<br/>network</a></li></ul>
</div>
<div data-role="footer" data-theme="a"> 
			<h6 class="footertext">&copy Rideshare-Ke</h6>
		</div>
</body>
</html>'''
      self.response.out.write(header+content+footer)

   def post(self):
      #check if user session is valid before proceeding ...
      useremail = ''
      userprofileimage = ''
      image = ''
      user = users.get_current_user()
      if not user:
         self.redirect(users.create_login_url(self.request.uri))
      else:
         useremail = users.get_current_user().email()
         #get userdetails ...
         query = Userstable.all()
         query.filter('useremail',useremail)
         queryresults = query.fetch(1,0)
         if not queryresults:
            donothing = ''
         else:
            for user in queryresults:
               userprofileimage = user.userprofileimage
      #upload user profile image ...
      try:
         image = images.resize(self.request.get('image'),200,200)
      except:
         image = ''
      query = Userstable.all()
      query.filter('useremail',useremail)
      queryresults = query.fetch(1,0)
      for user in queryresults:
         user.username = self.request.get('username')
         user.userphonenumber = self.request.get('userphonenumber')
         user.userpreferences = self.request.get('userpreferences')
         if image == '':
            user.userprofileimage = userprofileimage
         else:
            user.userprofileimage = db.Blob(image)
         user.put()
         self.redirect('/myaccount')
#end class Myaccount ...
