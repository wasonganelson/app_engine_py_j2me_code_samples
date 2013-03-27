from google.appengine.ext import webapp
from database import * #need this module to populate datastore ...

class Mapagentatmpage(webapp.RequestHandler):
   def get(self):
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
			mpesa finder
		</title> 
	</head> 
	<body>
		<div data-role="page"  id="mapagentatm"> 
			<div data-role="header" data-theme="a">
				<div class="headertext"> 
				map
				</div>
			</div>'''
      
      content = '''<div class="content" data-role="content" data-theme="c">
<form id="" action="/mapagentatm" method="post" enctype="multipart/form-data">
 %s<br/><br/>
 <label for="businessname"><b>business name:</b></label>
 <textarea cols="40" rows="8" name="businessname" id="businessname"></textarea><br/>
 <label for="latitude"><b>latitude:</b></label>
 <input type="text" name="latitude" id="latitude" value="0.0" readonly /><br/>
 <label for="longitude"><b>longitude:</b></label>
 <input type="text" name="longitude" id="longitude" value="0.0" readonly /><br/>
 <label for="category"><b>category:</b></label>
     <select name="category" id="category" data-native-menu="false">
	    <option value="agent.png">mpesa agent</option>
            <option value="atm.png">mpesa atm</option>
 </select><br/>
 <input type="submit" value="submit" data-inset="true" data-theme="c"/><br/>
</form>
<ul data-role="listview" data-inset="false" data-theme="a"> 
					<li> 
						<a href="/"> 
							back
						</a> 
					</li> 
                  </ul>
</div>'''%(self.request.get('error'))
      footer = '''<div data-role="footer" data-theme="a"> 
			<div class="footertext"> 
			&copy mpesa finder
			</div> 
		</div> 
		</div> 
	</body> 
</html>'''
      self.response.out.write(header+content+footer)
   def post(self):
      businessname = self.request.get('businessname')
      latitude = self.request.get('latitude')
      longitude = self.request.get('longitude')
      businesstype = self.request.get('category')
      if businessname == '' or businesstype == '':
        self.redirect('/mapagentatm?error="error! fill in all required details"')
      else:
         primaryid = 0
         #get last primaryid ...
         query = Agentatmtable.all()
         query.order('-primaryid') #order by primaryid desc ... most recent to least recent ...
         queryresults = query.fetch(1,0)
         if not queryresults:
            primaryid = 1
         else:
            for agentatm in queryresults:
               primaryid = agentatm.primaryid+1
         #upload agent or atm details to datastore ...
         agentatm = Agentatmtable()
         agentatm.primaryid = primaryid
         agentatm.businessname = businessname
         agentatm.latitude = latitude
         agentatm.longitude = longitude
         agentatm.businesstype = businesstype
         agentatm.verified = 'no'
         agentatm.put()
         self.redirect('/mapagentatm?error="thank you for having helped map an mpesa agent or mpesa enabled atm, details will still have to be verified."')
#end class Mapagentatmpage ...

