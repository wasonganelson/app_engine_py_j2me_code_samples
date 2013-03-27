from google.appengine.ext import webapp
from database import * #need this module to access datastore ...
from urlshortener import * #need this module to access urlshortener google api ...
import timestamper #contains timestamper def to get time of needit post ...

class Getneedit(webapp.RequestHandler):
   def get(self):
      #use key to fetch needit details from datastore ...
      needit = db.get(self.request.get("key"))
      needitkey = needit.key()
      need = needit.need
      urgency = needit.urgency
      offer = str(needit.offer)
      location = needit.location
      userphonenumber = needit.userphonenumber
      useremail = needit.useremail
      username = needit.username
      timestamp = needit.timestamp
      views = str(needit.views+1)
      #update needit views ...
      needit.views = int(views)
      needit.put()
      #use email to get user profile image ...
      query = Userstable.all()
      query.filter('useremail',useremail)
      queryresults = query.fetch(1,0)
      imagekey = ''
      for userdetails in queryresults:
         imagekey = userdetails.key()
      needitcontent = '''<div class="pagecontent">
            <div class="getneeditcontent">
              <img class="getneeditimage" src="/images/logo.png"/><br/>
              <div class="getneedittext">
                      <b>need: </b>%s<br/>
                      <b>urgency: </b>%s<br/>
                      <b>offer: </b>%s Ksh<br/>
                      <b>location: </b>%s<br/>
                      <b>contacts:</b><br/>
                      <a class="viewmorelink" href="mailto:%s">email:<br/> %s</a>,<br/> 
                      <a class="viewmorelink" href="tel:%s">telephone:<br/> %s</a><br/>
                      <b>posted: </b>%s<br/>
                      <b>views: </b>%s<br/>
              </div>
            </div>
            <div class="fbplugins">
               <div class="fb-share"><a name="fb_share" type="button_count" share_url="%s"></a></div>
               <script src="http://static.ak.fbcdn.net/connect.php/js/FB.Share" type="text/javascript">
               </script><br/>
<div>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a data-count="horizontal" data-text="%s" data-url="%s" data-counturl="%s" href="%s" class="twitter-share-button" data-lang="en">Tweet</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
<br/><br/></div>
               <!-- Place this tag where you want the share button to render. -->
               <div class="gplus"><div class="g-plus" href="%s" data-action="share"></div></div>
               <!-- Place this tag after the last share tag. -->
               <script type="text/javascript">
                  (function() {
                               var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
                               po.src = 'https://apis.google.com/js/plusone.js';
                               var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
                   })();
               </script><br/>
        </div>
        <br/><div class="fb-comments" data-href="%s" data-num-posts="10" data-width="320"></div>'''%(need, urgency, offer, location , useremail, useremail, userphonenumber, userphonenumber, timestamper.timestamper(timestamp), views, shorten(self.request.uri), need, shorten(self.request.uri), self.request.uri, shorten(self.request.uri), shorten(self.request.uri), self.request.uri)
      content = needitcontent
      
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
         <div id="fb-root"></div>
         <script>(function(d, s, id) {
            var js, fjs = d.getElementsByTagName(s)[0];
            if (d.getElementById(id)) return;
            js = d.createElement(s); js.id = id;
            js.src = "//connect.facebook.net/en_US/all.js#xfbml=1&appId=100125510130677";
            fjs.parentNode.insertBefore(js, fjs);
           }(document, 'script', 'facebook-jssdk'));
         </script>

	<div class="pageheader">need-it</div>
        <div class="needitsummaryendline"></div>'''
      
      footer = '''<div class="pagefooter">&copy need-it</div>
</body>
</html>'''
      self.response.out.write(header+content+footer)
#end class Getneedit ...
