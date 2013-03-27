from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.api import images
from database import * #need this module to access datastore ...

class Signuplogin(webapp.RequestHandler):
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
				<h3>signup</h3>
			</div>'''
      content = '''
<div data-role="content" data-theme="c">
            <div class="signupcontent">
              <img class="needitprofileimage" alt="upload image" src="/images/logo.png"/><br/>
              <div class="needitprofiletext">
                 <b>name:</b> %s<br/>
                 <b>email:</b> %s<br/>
              </div>
              <form method="post" action="/signuplogin" enctype="multipart/form-data">
                <br/>
                <b>to proceed, please upload a profile image:</b><input type="file" name="image" id="image" />
                <br/>
                <input class="button" type="submit" value="upload"/><br/><br/>
              </form>
            </div>
        </div>''' % (users.get_current_user().nickname(), users.get_current_user().email())
      footer = '''<div data-role="footer" data-theme="d"> 
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
      #upload user profile image ...
      image = images.resize(self.request.get('image'),200,200)
      newuser = Userstable()
      newuser.profileimage = db.Blob(image)
      newuser.useremail = users.get_current_user().email()
      newuser.put()
      self.redirect('/needitslogin')
#end class Signuplogin ...
