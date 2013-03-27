from google.appengine.ext import webapp
from database import * #need this module to access datastore ...
import timestamper #contains timestamper def to get time of needit post ...

class RideshareKenya(webapp.RequestHandler):
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
			Rideshare-Ke
		</title> 
	</head> 
	<body>
		<div data-role="page" data-theme="a"> 
			<div data-role="header" data-theme="a">
				<h3>Rideshare-Ke</h3>
			</div>
                <div data-role="content" data-theme="d">
                      <img class="logo" src="/images/logo.jpg"/>
                </div>
        '''
      
      footer = '''
<ul data-role="listview" data-inset="false" data-theme="a"> 
	<li> 
		<a href="/about"> 
			about
		</a> 
	</li>
        <li> 
		<a href="/help"> 
			help
		</a> 
	</li>
        <li> 
		<a href="/login"> 
			log in with gmail
		</a> 
	</li>
</ul>
<div data-role="footer" data-theme="a"> 
			<h6 class="footertext">&copy Rideshare-Ke</h6>
		</div>
</body>
</html>'''
      self.response.out.write(header+footer)
#end class RideshareKenya ...
