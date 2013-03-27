from google.appengine.ext import webapp
from database import * #need this module to populate datastore ...

class Upload(webapp.RequestHandler):
   def get(self):
      header = '''<!doctype html> 
<html>
	<head>
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
<form id="" action="/upload" method="post" enctype="multipart/form-data">
 %s<br/><br/>
 <label for="businessname"><b>business name:</b></label>
 <textarea cols="40" rows="8" name="businessname" id="businessname"></textarea><br/>
 <label for="latitude"><b>latitude:</b></label>
 <input type="text" name="latitude" id="latitude" value="0.0" /><br/>
 <label for="longitude"><b>longitude:</b></label>
 <input type="text" name="longitude" id="longitude" value="0.0" /><br/>
 <label for="category"><b>category:</b></label>
     <select name="category" id="category" data-native-menu="false">
	    <option value="agent.png">mpesa agent</option>
            <option value="atm.png">mpesa atm</option>
 </select><br/>
 <input type="submit" value="submit" data-inset="true" data-theme="c"/><br/>
</form>
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
        self.redirect('/upload?error="error! fill in all required details"')
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
         agentatm.verified = 'yes'
         agentatm.put()
         self.redirect('/upload?error="thank you for having helped map an mpesa agent or mpesa enabled atm, details will still have to be verified."')
#end class Upload ...
