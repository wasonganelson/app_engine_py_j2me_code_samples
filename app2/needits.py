from google.appengine.ext import webapp
from database import * #need this module to access datastore ...
import timestamper #contains timestamper def to get time of needit post ...

class Needits(webapp.RequestHandler):
   def get(self):
      offset = self.request.get('offset')
      if offset == '':
         offset = 0
      else:
         offset = int(offset)
      content = ''
      query = Needitstable.all()
      query.order('-timestamp') #order by timestamp desc ... most recent to least recent ...
      needits = query.fetch(10,offset)
      if not needits:
         content = '''<div class="pagecontent"><div class="resultsnotfound">sorry, no results found ...</div></div>'''
      else:
         for needit in needits:
            needitkey = needit.key()
            need = needit.need
            urgency = needit.urgency
            offer = str(needit.offer)
            location = needit.location
            userphonenumber = needit.userphonenumber
            useremail = needit.useremail
            username = needit.username
            timestamp = needit.timestamp
            views = str(needit.views)
            #use email to get user profile image ...
            query1 = Userstable.all()
            query1.filter('useremail',useremail)
            queryresults = query1.fetch(1,0)
            imagekey = ''
            for userdetails in queryresults:
               imagekey = userdetails.key()
            needitcontent = '''<div class="needitsummaryblock">
                  <img class="needitsummaryimage" src="/getimage?key=%s"/>
                  <div class="needitsummarytext">
                      <b>need: </b>%s<br/>
                      <b>urgency: </b>%s<br/>
                      <b>offer: </b>%s Ksh<br/>
                      <b>location: </b>%s<br/>
                      <b>by: </b>%s<br/>
                      <b>posted: </b>%s<br/>
                      <b>views: </b>%s &nbsp;&nbsp;&nbsp;<a class="viewmorelink" href="/getneedit?key=%s"> more...</a></div>
                </div>
                <div class="needitsummaryendline"></div>'''%(imagekey, need[:50]+" ......", urgency, offer, location , username, timestamper.timestamper(timestamp), views, needitkey)
            content = content + needitcontent
         moreneeditslink = ''
         queryresults = query.fetch(10,offset+10)
         if queryresults:
            moreneeditslink = '<div align="center"><a class="viewmorelink" href="/?offset=%d"><br/>more needits<br/><br/></a></div>'%(offset+10)
         content = '''<div class="pagecontent">''' + content + moreneeditslink + '''</div>'''
      
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
	<div class="pageheader">need-it</div>
        <div class="searchbox"><form method="get" action="/search">
           <input class="searchtextinput" type="text" id="searchkey" name="searchkey" value=""/>
           <input class="searchbutton" type="submit" value="search"/><br/><br/>
        </form></div>
        <div class="needitsummaryendline"></div>'''
      
      footer = '''
<div>
            <a class="footerlink" href="/"><div class="footerlinkitem"> needits >></div></a>
            <a class="footerlink" href="/about"><div class="footerlinkitem"> about >></div></a>
            <a class="footerlink" href="/login"><div class="footerlinkitem"> login >></div></a>
        </div>
	<div class="pagefooter">&copy need-it</div>
</body>
</html>'''
      self.response.out.write(header+content+footer)
#end class Needits ...
