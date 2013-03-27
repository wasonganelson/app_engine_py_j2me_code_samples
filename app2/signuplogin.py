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
      header = '''
<!DOCTYPE html PUBLIC "-//WAPFORUM//DTD XHTML Mobile 1.0//EN" "http://www.wapforum.org/DTD/xhtml-mobile10.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<meta name="HandheldFriendly" content="true" />
<meta name="viewport" content="width=device-width; initial-scale=1.0; minimum-scale=1.0; maximum-scale=1.0; user-scalable=0;" />
<style type="text/css">
</style>
<link type="text/css" rel="stylesheet" href="jscss/style.css" />
<script type="text/javascript">
var ua = navigator.userAgent;
var checker = {
                 iphone: ua.match(/(iPhone|iPod|iPad)/),
                 blackberry: ua.match(/BlackBerry/),
                 android: ua.match(/Android/)
                };
if (checker.android || checker.iphone || checker.blackberry)
{
}
else{window.location = "/error"}
</script>
<body>
	<div class="pageheader">signup</div>'''
      content = '''
<div class="pagecontent">
            <div class="signupcontent">
              <img class="needitprofileimage" alt="upload image" src="0.jpg"/><br/>
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
      footer = '''<div class="pagefooter">&copy need-it</div>
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
