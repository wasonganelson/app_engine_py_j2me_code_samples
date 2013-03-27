from google.appengine.ext import webapp

class Blacklist(webapp.RequestHandler):
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
	<div class="pageheader">need-it</div>'''
      content = '''
<div class="pagecontent">
          <div class="aboutcontent">sorry !, looks like you've been spamming the site and as a result you can not use this web-service. Consult needitkenya@gmail.com for help ...</div>
        </div>'''
      footer = '''<div class="pagefooter">&copy need-it</div>
</body>
</html>'''
      self.response.out.write(header+content+footer)
#end class Blacklist ...
