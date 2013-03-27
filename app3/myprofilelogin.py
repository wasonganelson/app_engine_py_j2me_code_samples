from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.api import images
from database import * #need this module to access datastore ...

class Myprofilelogin(webapp.RequestHandler):
   def get(self):
      #check if user session is valid before proceeding ...
      user = users.get_current_user()
      if not user:
         self.redirect(users.create_login_url(self.request.uri))
      else:
         x = ""
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
			need-it
		</title> 
	</head> 
	<body>
		<div data-role="page"> 
			<div data-role="header" data-theme="d">
				<h3>my profile</h3>
			</div>'''
      #get user details to display on page ...
      query = Userstable.all()
      query.filter('useremail',users.get_current_user().email())
      queryresults = query.fetch(1,0)
      imagekey = ''
      for userdetails in queryresults:
         imagekey = userdetails.key()
      content = '''
<div data-role="content" data-theme="c">
            <div class="signupcontent">
              <img class="needitprofileimage" alt="upload image" src="/getimage?key=%s"/><br/>
              <div class="needitprofiletext">
                 <b>name:</b> %s<br/>
                 <b>email:</b> %s<br/>
              </div>
              <form method="post" action="/myprofilelogin" enctype="multipart/form-data">
                <br/><b>upload new profile image :</b><input type="file" name="image" id="image" /><br/>
                <input class="button" type="submit" value="upload"/><br/><br/>
              </form>
            </div>
        </div>''' % (imagekey, users.get_current_user().nickname(), users.get_current_user().email())
      footer = '''
<ul data-role="listview" data-inset="false" data-theme="c" data-icon="false"> 
	<li> 
		<a href="/needitslogin"> 
			needits
		</a> 
	</li>
        <li> 
		<a onclick="url='/needitsaroundmelogin';getneeditsaroundme();"> 
			needits around me
		</a> 
	</li> 
	<li> 
		<a href="/about"> 
			about
		</a> 
	</li>
        <li> 
		<a href="/postneeditlogin"> 
			post needit
		</a> 
	</li>
        <li> 
		<a href="/myneeditslogin"> 
			my needits
		</a> 
	</li>
        <li> 
		<a href="/myprofilelogin"> 
			my profile
		</a> 
	</li>
        <li> 
		<a href="/logout"> 
			logout
		</a> 
	</li>
</ul>
<div data-role="footer" data-theme="d"> 
			<h6 class="footertext">&copy need-it</h6>
		</div>
</body>
</html>'''
      self.response.out.write(header+content+footer)

   def post(self):
      #check if user session is valid before proceeding ...
      user = users.get_current_user()
      if not user:
         self.redirect(users.create_login_url(self.request.uri))
      else:
         x = ""
      #check that user is not in blacklist ...
      useremail = user.email()
      query = Blacklisttable.all()
      query.filter('useremail',useremail)
      queryresults = query.fetch(1,0)
      if queryresults:# if in blacklist, redirect to blacklist page ...
         self.redirect("/blacklist")
      #search for user in datastore and update profileimage ...
      else:
         query = Userstable.all()
         query.filter('useremail',users.get_current_user().email())
         queryresults = query.fetch(1,0)
         for userdetails in queryresults:
            image = images.resize(self.request.get('image'),200,200)
            userdetails.profileimage = db.Blob(image)
            userdetails.put()
         self.redirect('/myprofilelogin')
#end class Myprofilelogin ...
