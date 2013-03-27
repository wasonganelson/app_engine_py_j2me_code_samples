from google.appengine.ext import webapp

class Helplogin(webapp.RequestHandler):
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
			</div>'''
      content = '''
<div data-role="content" data-theme="a">
          <h5><br/>still under construction .... just enable GPS to use the app ... <br/><br/>1. login using gmail<br/><br/>2. upload profile pic<br/><br/>3. post ride offer or seek lift from people around you ... <br/><br/>4. contact your fellow carpooler.</h5>
        </div>
'''
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
#end class Helplogin ...
