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
	<div class="pageheader">my profile</div>'''
      #get user details to display on page ...
      query = Userstable.all()
      query.filter('useremail',users.get_current_user().email())
      queryresults = query.fetch(1,0)
      imagekey = ''
      for userdetails in queryresults:
         imagekey = userdetails.key()
      content = '''
<div class="pagecontent">
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
<div>
            <a class="footerlink" href="/needitslogin"><div class="footerlinkitem"> needits >></div></a>
            <a class="footerlink" href="/about"><div class="footerlinkitem"> about >></div></a>
            <a class="footerlink" href="/postneeditlogin"><div class="footerlinkitem"> post needit >></div></a>
            <a class="footerlink" href="/myneeditslogin"><div class="footerlinkitem"> my needits >></div></a>
            <a class="footerlink" href="/myprofilelogin"><div class="footerlinkitem"> my profile >></div></a>
            <a class="footerlink" href="/logout"><div class="footerlinkitem"> logout >></div></a>
        </div>
        <div class="pagefooter">&copy need-it</div>
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
