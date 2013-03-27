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
			mpesa finder
		</title> 
	</head> 
	<body>
		<div data-role="page"> 
			<div data-role="header" data-theme="a">
                                <div class="headertext"> 
                                   about
                                </div>
				</div>'''
      
      content = '''<div class="content" data-role="content" data-theme="a"><b>Ever found yourself in a situation where you need to make some mpesa withdrawal or deposit and you don't want to go asking every Tom, Dick and Harry where the nearest agent or mpesa enabled atm is located ?<br/><br/>Look no further, let the mpesa finder app do the searching for you and avoid the risk of indirectly informing strangers your intention to make a cash withdrawal or deposit.<br/><br/>App made by mpesafinder@gmail.com</b></div>
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
#end class Aboutpage ...
