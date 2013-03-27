from google.appengine.ext import webapp

class About(webapp.RequestHandler):
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
			need-it
		</title> 
	</head> 
	<body>
		<div data-role="page"> 
			<div data-role="header" data-theme="d">
				<h3>about</h3>
			</div>'''
      content = '''
<div data-role="content" data-theme="c">
          <h5>Have you ever found yourself in a situation whereby you need something and that you unfortunately do not have ? For intance, you are in the library, your laptop is fast running out of charge only for you to realize that you left your charger in the room or at home, look no further. Whatever your need is, just "need-it" at need-it.appspot.com.<br/><br/>
  <b>needit</b> is a mobilephone-based, location-aware, buyer-driven marketplace. Think of it as different kind of marketplace where rather than find sellers putting up items or services for sale, you find buyers who are ready to pay to have their various needs met.<br/><br/>
  <b>terms and conditions: </b>settlement of transactions and handling of payments is done entirely at the discretion of the involved parties, need-it only provides a platform through which the parties meet and no commissions whatsoever are charged on the transactions settled via need-it. Its a free web-service.<br/><br/>
   <b>sign up: </b>use your existing gmail account to sign up and start posting your "need-its". Use your android or iphone native browser for an optimized experience. </h5>
        </div>'''
      footer = '''<div data-role="footer" data-theme="d"> 
			<h6 class="footertext">&copy need-it</h6>
		</div>
</body>
</html>'''
      self.response.out.write(header+content+footer)
#end class About ...
