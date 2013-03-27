from google.appengine.ext import webapp
from database import * #need this module to populate datastore ...

class Helppage(webapp.RequestHandler):
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
			mpesa finder
		</title> 
	</head> 
	<body>
		<div data-role="page"> 
			<div data-role="header" data-theme="a">
				<div class="headertext"> 
				help
				</div>
			</div>'''
      
      content = '''<div class="content" data-role="content" data-theme="a"><b>mpesa finder is a location based application that helps you find and view on a map mpesa agent shops and mpesa enabled atm's around you.<br/><br/>To use the app, go to 'My Location' menu in your phone's System Settings and enable GPS. If you are having trouble with GPS, then enable use of wirless network and wifi for geolocation and ensure your internet connection works fine.<br/><br/>mpesa finder aims to map all mpesa agents and mpesa enabled atms through crowdsourcing, however all uploads will undergo verification checks</b></div>
                  <ul data-role="listview" data-inset="false" data-theme="a"> 
					<li> 
						<a href="/"> 
							back
						</a> 
					</li> 
                  </ul>'''
      footer = '''<div data-role="footer" data-theme="a"> 
			<div class="footertext"> 
			&copy mpesa finder
			</div> 
		</div> 
		</div> 
	</body> 
</html>'''
      self.response.out.write(header+content+footer)
#end class Helppage ...

