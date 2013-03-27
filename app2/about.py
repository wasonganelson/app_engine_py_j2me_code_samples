from google.appengine.ext import webapp

class About(webapp.RequestHandler):
   def get(self):
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
	<div class="pageheader">about</div>'''
      content = '''
<div class="pagecontent">
          <div class="aboutcontent">Did you fail to secure accomodation from SWA and you are in dire need of a room ?, or could it be that you are in the library, your laptop is fast running out of charge only for you to realize that you left your charger in the room or at home, look no further. Whatever your need is, just "need-it" at need-it.appspot.com.<br/><br/>
  <b>needit</b> is a mobilephone-based buyer-driven marketplace. Think of it as different kind of marketplace where rather than find sellers putting up items or services for sale, you find buyers who are ready to pay to have their various needs met.<br/><br/>
  <b>terms and conditions: </b>settlement of transactions and handling of payments is done entirely at the discretion of the involved parties, need-it only provides a platform through which the parties meet and no commissions whatsoever are charged on the transactions settled via need-it. Its a free web-service.<br/><br/>
   <b>sign up: </b>use your existing gmail account to sign up and start posting your "need-its". Use your android or iphone native browser for an optimized experience. </div>
        </div>'''
      footer = '''<div class="pagefooter">&copy need-it</div>
</body>
</html>'''
      self.response.out.write(header+content+footer)
#end class About ...
