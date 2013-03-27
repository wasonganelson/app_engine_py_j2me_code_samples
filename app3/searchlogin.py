from google.appengine.api import users
from google.appengine.ext import webapp
from database import * #need this module to access datastore ...
import timestamper #contains timestamper def to get time of needit post ...

class Searchlogin(webapp.RequestHandler):
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
      needits = query.fetch(1000,offset)
      if not needits:
         content = '''<div data-role="content" data-theme="c"><div class="resultsnotfound">sorry, no results found ...</div></div>'''
      else:
         resultcount = 0 #keep track of result count ...
         for needit in needits:
            if(resultcount > 19):break #return best 20 results of the first 1000 needits ...
            needitkey = needit.key()
            need = needit.need
            offer = str(needit.offer)
            useremail = needit.useremail
            #use details above to search for searchkeys ...
            searchkeysfound = False
            searchkeys = self.request.get('searchkey').split(' ')
            for searchkey in searchkeys:
               if(need.lower().find(searchkey.lower())>-1):searchkeyfound = True
               else:searchkeyfound = False
            if(searchkeyfound == False):continue
            else:resultcount += 1
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
         if(content == ''):content = '''<div data-role="content" data-theme="c"><div class="resultsnotfound">sorry, no results found ...</div></div>'''
         else:content = '''<div data-role="content" data-theme="c">''' + content + '''</div>'''
      
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
           <div class="ui-block-a"><input class="searchtextinput" type="text" id="searchkey" name="searchkey" value="%s"/></div>
           <div class="ui-block-b"><input class="searchbutton" type="submit" value="search"/><br/><br/></div>
           </div>
        </form></div>'''%(self.request.get('searchkey'))
      
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
#end class Searchlogin ...
