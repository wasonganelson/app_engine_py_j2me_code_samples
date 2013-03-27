from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.api import images
from database import * #need this module to populate datastore ...
import time #need this for timestamping ...

class Postneeditlogin(webapp.RequestHandler):
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
	<div class="pageheader">post</div>'''
      content = '''
<div class="pagecontent">
          <div class="postcontent">
            <form method="post" action="/postneeditlogin">
               fill in all fields ...<br/><br/>
               needit :<br/><textarea class="postcontenttextarea" id="need" name="need">I need </textarea><br/><br/>
               urgency(now, asap, by weekend ...) :<br/><textarea class="postcontenttextarea" id="urgency" name="urgency"></textarea><br/><br/>
               offer(min of Ksh 50) :<br/><input class="postcontenttextarea" type="number" id="offer" name="offer" value="50"/><br/><br/>
               where u at ?(parki, mamlaka, add, stella, box, chiromo ...) :<br/><textarea class="postcontenttextarea" id="location" name="location"></textarea><br/><br/>
               telephone contact (optional):<br/><textarea class="postcontenttextarea" id="userphonenumber" name="userphonenumber"></textarea><br/><br/>
               email contact (not editable):<br/><textarea class="postcontenttextarea" id="useremail" name="useremail" readonly>%s</textarea><br/><br/>
               username (not editable):<br/><textarea class="postcontenttextarea" id="username" name="username" readonly>%s</textarea><br/>
               <input class="button" type="submit" value="post"/><br/><br/>
            </form>
          </div>
        </div>''' % (users.get_current_user().email(), users.get_current_user().nickname())
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
      #get user needit post ...
      else:
         need = self.request.get('need').strip()
         urgency = self.request.get('urgency').strip()
         offer = self.request.get('offer').strip()
         location = self.request.get('location').strip()
         userphonenumber = self.request.get('userphonenumber').strip()
         useremail = self.request.get('useremail').strip()
         username = self.request.get('username').strip()
         timestamp = int(time.time())
         views = 2
         #validate user needit ...
         if(need == '' or urgency == '' or location == ''):
            self.redirect('/postneeditlogin')
         else:
            needit = Needitstable()
            needit.need = need
            needit.urgency = urgency
            needit.offer = int(offer)
            needit.location = location
            needit.userphonenumber = userphonenumber
            needit.useremail = useremail
            needit.username = username
            needit.timestamp = timestamp
            needit.views = views
            needit.put()
            self.redirect('/needitslogin')
#end class Postneeditlogin ...
