from google.appengine.ext import webapp

class Campusespage(webapp.RequestHandler):
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
      content = '''<div class="content" data-role="content" data-theme="d"> 
			<ul data-role="listview" data-filter="true" data-filter-placeholder="search campus" data-theme="a"> 
					<li> 
						<a href="/campusnewspage?offset=0&campustag=1"> 
				                  Africa Nazarene
						</a> 
					</li> 
                                        <li> 
						<a href="/campusnewspage?offset=0&campustag=2"> 
						  Baraton
						</a> 
					</li> 
                                        <li> 
						<a href="/campusnewspage?offset=0&campustag=3"> 
					           CUEA
						</a> 
					</li> 
                                        <li> 
						<a href="/campusnewspage?offset=0&campustag=4"> 
						   Daystar
						</a> 
					</li> 
                                        <li> 
						<a href="/campusnewspage?offset=0&campustag=5"> 
					           Egerton
						</a> 
					</li> 
                                        <li> 
						<a href="/campusnewspage?offset=0&campustag=6"> 
					           JKUAT
						</a> 
					</li> 
                                        <li> 
						<a href="/campusnewspage?offset=0&campustag=7"> 
						     Kabarak
						</a> 
					</li> 
                                        <li> 
						<a href="/campusnewspage?offset=0&campustag=8"> 
						     KCA
						</a> 
					</li> 
                                        <li> 
						<a href="/campusnewspage?offset=0&campustag=9"> 
					             KEMU
						</a> 
					</li> 
                                        <li> 
						<a href="/campusnewspage?offset=0&campustag=10"> 
					             KU
						</a> 
					</li>
                                        <li> 
						<a href="/campusnewspage?offset=0&campustag=11"> 
					           Maseno
						</a> 
					</li> 
                                        <li> 
						<a href="/campusnewspage?offset=0&campustag=12"> 
					            Masinde Muliro
						</a> 
					</li> 
                                        <li> 
						<a href="/campusnewspage?offset=0&campustag=13"> 
						    Moi
						</a> 
					</li> 
                                        <li> 
						<a href="/campusnewspage?offset=0&campustag=14"> 
						     Strathmore
						</a> 
					</li> 
                                        <li> 
						<a href="/campusnewspage?offset=0&campustag=15"> 
						     UoN
						</a> 
					</li>
                                        <li> 
						<a href="/campusnewspage?offset=0&campustag=16"> 
						     USIU
						</a> 
					</li>
                                        <li> 
						<a href="/"> 
						     home
						</a> 
					</li>
				</ul> 
		</div>'''
      footer = '''<div data-role="footer" data-theme="a"> 
			<div class="footertext"> 
			&copy CampusDaily
			</div> 
		</div> 
		</div> 
	</body> 
</html>'''
      self.response.out.write(header+content+footer)
#end class Campusespage ...

