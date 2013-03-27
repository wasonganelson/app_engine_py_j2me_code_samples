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
		<div data-role="page" id="postneeditpage"> 
			<div data-role="header" data-theme="d">
				<h3>post</h3>
			</div>'''
      content = '''
<div data-role="content" data-theme="c">
          <div class="postcontent">
            <form method="post" action="/postneeditlogin">
               fill in all fields ...<br/><br/>
               needit :<br/><textarea id="need" name="need">I need </textarea><br/>
               urgency(asap, by weekend ...) :<br/><input type="text id="urgency" name="urgency"><br/>
               offer(min of Ksh 50) :<br/><input type="number" id="offer" name="offer" value="50"/><br/>
               telephone contact (optional) :<br/><input type="text" id="userphonenumber" name="userphonenumber" /><br/>
               email contact (not editable) :<br/><input type="text" id="useremail" name="useremail" value=%s readonly /><br/>
               username (not editable) :<br/><input type="text" id="username" name="username" value=%s readonly /><br/>
               latitude (not editable) :<br/><input type="text" id="latitude" name="latitude" readonly/><br/>
               longitude (not editable) :<br/><input type="text" id="longitude" name="longitude" readonly/><br/>
               <input class="button" type="submit" value="post"/><br/><br/>
            </form>
          </div>
        </div>''' % (users.get_current_user().email(), users.get_current_user().nickname())
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
         latitude = self.request.get('latitude').strip()
         longitude = self.request.get('longitude').strip()
         userphonenumber = self.request.get('userphonenumber').strip()
         useremail = self.request.get('useremail').strip()
         username = self.request.get('username').strip()
         timestamp = int(time.time())
         views = 2
         #validate user needit ...
         if(need == '' or urgency == ''):
            self.redirect('/postneeditlogin')
         else:
            needitprimaryid = ''
            #get last primaryid ...
            query = Needitstable.all()
            query.order('-timestamp') #order by timestamp desc ... most recent to least recent ...
            queryresults = query.fetch(1,0)
            if not queryresults:
               needitprimaryid = '1'
            else:
               for article in queryresults:
                  needitprimaryid = str(int(article.primaryid)+1)
            needit = Needitstable()
            needit.primaryid = needitprimaryid
            needit.need = need
            needit.urgency = urgency
            needit.offer = int(offer)
            needit.latitude = latitude
            needit.longitude = longitude
            needit.userphonenumber = userphonenumber
            needit.useremail = useremail
            needit.username = username
            needit.timestamp = timestamp
            needit.views = views
            needit.put()
            self.redirect('/needitslogin')
#end class Postneeditlogin ...
