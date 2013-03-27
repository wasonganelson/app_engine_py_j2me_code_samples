from google.appengine.ext import webapp
from database import * #need this module to access datastore ...
import timestamper #contains timestamper def to get time of needit post ...
import calculatedistance #contains calculatedistance ...

class Getliftseeker(webapp.RequestHandler):
   def get(self):
      #use key to fetch rideshare details from datastore ...
      userlatitude = self.request.get('userlatitude')
      userlongitude = self.request.get('userlongitude')
      liftseeker = db.get(self.request.get("key"))
      departurepoint = liftseeker.departurepoint
      destinationpoint = liftseeker.destinationpoint
      costperseat = liftseeker.costperseat
      departuretime = liftseeker.departuretime
      timestamp = liftseeker.timestamp
      useremail = liftseeker.useremail
      username = ''
      userphonenumber = ''
      userpreference = ''
      latitude = liftseeker.latitude
      longitude = liftseeker.longitude
      url = "/viewmap?userlatitude=%s&userlongitude=%s&latitude=%s&longitude=%s&back=%s&key=%s" % (userlatitude, userlongitude, latitude, longitude, "getliftseeker", self.request.get("key"))
      distance = calculatedistance.calculatedistance(userlatitude, userlongitude, latitude, longitude)
      #use email to get user profile image ...
      query = Userstable.all()
      query.filter('useremail',useremail)
      queryresults = query.fetch(1,0)
      imagekey = ''
      for userdetails in queryresults:
         imagekey = userdetails.key()
         username = userdetails.username
         userpreferences = userdetails.userpreferences
         userphonenumber = userdetails.userphonenumber
      liftseekercontent = '''<div class="ridesharedsummaryblock">
            <img class="getridesharedsummaryimage" src="/getimage?key=%s"/>
            <div class="getridesharedsummarytext">
                <span class="fromto2">contact: </span><br/><a class="viewmorelink2" href="">%s</a><br/><br/>
                <span class="fromto2">email: </span><br/><a class="viewmorelink2" href="mailto:%s">%s</a><br/><br/>
                <span class="fromto2">telephone: </span><br/><a class="viewmorelink2" href="tel:%s">%s</a><br/><br/>
            </div>
                <a class="viewmorelink3" href="%s">view map directions(find me here)</a><br/><br/>
                <span class="fromto2">seeking lift from:</span> %s <br/><br/>
                <span class="fromto2">to:</span> %s<br/><br/>
                <span class="fromto2">will pay(KES):</span> %s<br/><br/>
                <span class="fromto2">preferred departure time(within the next):</span> %s<br/><br/>
                <span class="fromto2">preferences:</span> %s<br/><br/>
                <span class="fromto2">posted:</span> %s meters away<br/><br/>
            </div>
            <div class="ridesharedsummaryendline"></div>'''%(imagekey, username, useremail, useremail, userphonenumber, userphonenumber, url, departurepoint, destinationpoint, costperseat, timestamper.timestamper1(departuretime, timestamp), userpreferences, distance)
      content = ''
      content = '<div class="content" data-role="content" data-theme="a">' + liftseekercontent + '</div>'
      
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
			Rideshare-Ke
		</title> 
	</head> 
	<body>
                <div data-role="page" data-theme="a"> 
			<div data-role="header" data-theme="a">
                                <h5 class="headertext">Rideshare-Ke</h5>
			</div>'''
      
      footer = '''
<ul data-role="listview" data-inset="false" data-theme="a"> 
	<li>
		<a href="/liftseekersaroundme?offset=0&userlatitude=%s&userlongitude=%s">
			back
		</a> 
	</li>
</ul>
<div data-role="footer" data-theme="a"> 
			<h6 class="footertext">&copy Rideshare-Ke</h6>
		</div>
</body>
</html>''' % (userlatitude, userlongitude)
      self.response.out.write(header+content+footer)
#end class Getliftseeker ...
