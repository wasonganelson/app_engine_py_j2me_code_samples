from google.appengine.api import users
from google.appengine.ext import webapp
from database import * #need this module to access datastore ...
import timestamper #contains timestamper def to get time of needit post ...

class Needitslogin(webapp.RequestHandler):
   def get(self):
      #check if user session is valid before proceeding ...
      user = users.get_current_user()
      if not user:
         self.redirect(users.create_login_url(self.request.uri))
      else:
         x = ""
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
         content = '''<div data-role="content" data-theme="c"><div class="resultsnotfound">sorry, no results found ...</div></div>'''
      else:
         for needit in needits:
            needitkey = needit.key()
            need = needit.need
            offer = str(needit.offer)
            useremail = needit.useremail
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
                      <b>offer: </b>%s Ksh<br/>
                      <b>posted: </b>%s<br/>
                      <b>views: </b>%s &nbsp;&nbsp;&nbsp;<a class="viewmorelink" href="/getneedit?key=%s"> more...</a></div>
                </div>
                <div class="needitsummaryendline"></div>'''%(imagekey, need[:50]+" ......", offer, timestamper.timestamper(timestamp), views, needitkey)
            content = content + needitcontent
         moreneeditslink = ''
         queryresults = query.fetch(10,offset+10)
         if queryresults:
             moreneeditslink = '<div><a class="viewmorelink" href="/needitslogin?offset=%d">more needits >></a></div>'%(offset+10)
         content = '''<div data-role="content" data-theme="c">''' + content + moreneeditslink + '''</div>'''
      
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
				<h3>need-it</h3>
			</div>
        <div class="searchbox"><form method="get" action="/searchlogin">
           <div class="ui-grid-a">
           <div class="ui-block-a"><input class="searchtextinput" type="text" id="searchkey" name="searchkey" value=""/></div>
           <div class="ui-block-b"><input class="searchbutton" type="submit" value="search"/><br/><br/></div>
           </div>
        </form></div>'''
      
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
#end class Needitslogin ...
