from google.appengine.api import users
from google.appengine.ext import webapp
from database import * #need this module to populate datastore ...
import time #need this for timestamping ...

class Seekliftlogin(webapp.RequestHandler):
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
		<script type="text/javascript" src="jscss/jqui.js"></script>
                <script type="text/javascript" src="jscss/custom.js"></script> 
		<script type="text/javascript" src="jscss/jqmjs.js"></script>
<script>
$(function() {
var itemList = [
    "Alfa","Alpha","Bravo","Charlie","Delta","Echo","Foxtrot","Golf","Hotel",
    "India","Juliett","Juliet","Kilo","Lima","Mike","November","Oscar","Papa"
    ];
    $("#departurepoint").autocomplete({
    source: itemList
    });
    $("#destinationpoint").autocomplete({
    source: itemList
    });
});
</script>                 
                <title> 
			Rideshare-Ke
		</title> 
	</head> 
	<body>
		<div data-role="page" id="seekliftloginpage" data-theme="a"> 
			<div data-role="header" data-theme="a">
				<h3>Rideshare-Ke</h3>
			</div>'''
      useremail = users.get_current_user().email()
      content = '''
<div data-role="content" data-theme="a">
          <div class="postcontent">
            <form method="post" action="/seekliftlogin">
               fill in all fields ...<br/><br/>
               seeking a lift from :<br/><input type="text class="ui" id="departurepoint" name="departurepoint" value="ihub, ngong rd" onclick=this.value='' /><br/>
               to :<br/><input type="text class="ui" id="destinationpoint" name="destinationpoint" value="ihub, ngong rd" onclick=this.value='' /><br/>
               <label for="departuretime">preferred time of departure:</label>
               <select name="departuretime" id="departuretime" data-native-menu="false">
	         <option value="900">within 15 min</option>
                 <option value="1800">within 30 min</option>
                 <option value="2700">within 45 min</option>
                 <option value="3600">within 1 hr</option>
               </select><br/>
               willing to pay (Ksh) :<br/><input type="number" id="costperseat" name="costperseat" value="100"/><br/>
               <input type="hidden" id="useremail" name="useremail" value=%s />
               <input type="hidden" id="latitude" name="latitude" value="0"/>
               <input type="hidden" id="longitude" name="longitude" value="0" /><br/>
               <input class="button" type="submit" value="post"/><br/><br/>
            </form>
          </div>
        </div>''' % (useremail)
      footer = '''
<ul data-role="listview" data-inset="false" data-theme="a"> 
	<li>
		<a onclick="url='/ridessharedaroundme';getridessharedaroundme();"> 
			rides shared
		</a> 
	</li>
        <li> 
		<a onclick="url='/liftseekersaroundme';getliftseekersaroundme();"> 
			lift seekers
		</a> 
	</li>
        <li> 
		<a href="/postridelogin"> 
			share ride
		</a> 
	</li>
        <li> 
		<a href="/seekliftlogin"> 
			seek lift
		</a> 
	</li>
        <li> 
		<a href="/aboutlogin"> 
			about
		</a> 
	</li>
        <li> 
		<a href="/helplogin"> 
			help
		</a> 
	</li>
        <li> 
		<a href="/logout"> 
			log out
		</a> 
	</li>
</ul>
<div data-role="navbar" data-theme="a">
	<ul><li><a href="/ridesharekenyalogin">main<br/>menu</a></li>
	<li><a href="/myaccount">my<br/>account</a></li>
	<li><a href="/mynetwork">my<br/>network</a></li>
	<li><a href="/addtonetwork">add to<br/>network</a></li></ul>
</div>
<div data-role="footer" data-theme="a"> 
			<h6 class="footertext">&copy Rideshare-Ke</h6>
		</div>
</body>
</html>'''
      self.response.out.write(header+content+footer)

   def post(self):
      #check if user session is valid before proceeding ...
      user = users.get_current_user()
      if not user:
         self.redirect(users.create_login_url(self.request.uri))
      #get user post ...
      else:
         departurepoint = self.request.get('departurepoint').strip()
         destinationpoint = self.request.get('destinationpoint').strip()
         departuretime = int(self.request.get('departuretime').strip())
         costperseat = int(self.request.get('costperseat').strip())
         useremail = self.request.get('useremail').strip()
         latitude = self.request.get('latitude').strip()
         longitude = self.request.get('longitude').strip()
         timestamp = int(time.time())
         #validate user post ...
         if(departurepoint == '' or destinationpoint == ''):
            self.redirect('/seekliftlogin')
         else:
            primaryid = ''
            #get last primaryid ...
            query = Liftseekerstable.all()
            query.order('-timestamp') #order by timestamp desc ... most recent to least recent ...
            queryresults = query.fetch(1,0)
            if not queryresults:
               primaryid = 1
            else:
               for seekliftposts in queryresults:
                  primaryid = seekliftposts.aaprimaryid+1
            seekliftpost = Liftseekerstable()
            seekliftpost.aaprimaryid = primaryid
            seekliftpost.departurepoint = departurepoint
            seekliftpost.destinationpoint = destinationpoint
            seekliftpost.departuretime = departuretime
            seekliftpost.costperseat = costperseat
            seekliftpost.useremail = useremail
            seekliftpost.latitude = latitude
            seekliftpost.longitude = longitude
            seekliftpost.timestamp = timestamp
            seekliftpost.status = 'active'
            seekliftpost.put()
            url = '/liftseekersaroundme?offset=0&userlatitude=%s&userlongitude=%s' % (latitude, longitude)
            self.redirect(url)
#end class Seekliftlogin ...
