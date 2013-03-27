from google.appengine.ext import webapp

class Aboutpage(webapp.RequestHandler):
   def get(self):
      header = '''<!doctype html> 
<html manifest="/appcachedir/app.appcache">
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
			CampusDaily
		</title> 
	</head> 
	<body>
		<div data-role="page"> 
			<div data-role="header" data-theme="a">
                                <div class="headertext"> 
				CampusDaily
				</div>
                        </div>'''
      content = '''<div class="content" data-role="content" data-theme="a"><h5>CampusDaily is a digital, publication that aims to keep kenyan campus going students and the general public, upclose and updated on news and events taking place in kenyan campuses.<br/><br/>Every attempt possible is made to ensure that published articles are free from nudity, profanity and inflammatory sentiments targeted at any race, religion, nationality, sexual orientation or ethnic group.<br/><br/>News:<br/><br/>CampusDaily accepts news articles submitted to campusdailykenya@gmail.com . All news submitted will be reviewed with a gentle hand (spelling and grammar checking) by the editorial team at CampusDaily. Are you organizing for an event ? Have the event listed on CampusDaily by mailing us all necessary event details (name, venue, entry requirements, contact persons details). <br/><br/>Break News:<br/><br/> To harness the power of citizen journalism, campusdaily allows for upload of news content as it happens. The uploads will still be subject to the above mentioned terms and conditions. User should strive to ensure that their news uploads are of an acceptable quality level or risk having their work discarded as spam.<br/><br/> Access the web app from your dolphin or native browser on android or safari browser on your iOS device for an optimised experience.</div>'''
      footer = '''<div data-role="footer" data-theme="a"> 
			<div class="footertext"> 
			&copy CampusDaily
			</div> 
		</div> 
		</div> 
	</body> 
</html>'''
      self.response.out.write(header+content+footer)
#end class Aboutpage ...
