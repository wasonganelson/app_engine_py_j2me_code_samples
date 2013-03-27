from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.api import images
from database import * #need this module to populate datastore ...
import time #need this for timestamping ...

class Breaknewspage(webapp.RequestHandler):
   def get(self):
      user = users.get_current_user()
      if not user:
         self.redirect(users.create_login_url(self.request.uri))
      else:
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
			CampusDaily
		</title> 
	</head> 
	<body>
		<div data-role="page" id="breaknewspage"> 
			<div data-role="header" data-theme="a">
                                <div class="headertext"> 
				CampusDaily
				</div>
                        </div>'''
      
         content = '''<div data-role="content" data-theme="a">
<form id="" action="/breaknews" method="post" enctype="multipart/form-data">
 fill in all fields and select an image for upload before submitting post ...<br/><br/>
 <div>
     <label for="content">what's happening ?</label>
     <textarea cols="40" rows="8" name="content" id="content"></textarea><br/>
 </div>
 <div>
      <label for="image">upload image:</label>
      <input type="file" name="image" id="image" /><br/>
 </div>
 <div>
     <label for="category">news category:</label>
     <select name="category" id="category" data-native-menu="false">
	    <option value="general news">general news</option>
            <option value="events">events</option>
            <option value="sports">sports</option>
            <option value="politics">politics</option>
     </select><br/>
 </div>
 <div>
     <label for="campustag">campus tag:</label>
     <select name="campustag" id="campustag" data-native-menu="false">
	    <option value="1">Africa Nazarene</option>
            <option value="2">Baraton</option>
            <option value="3">CUEA</option>
            <option value="4">Daystar</option>
            <option value="5">Egerton</option>
            <option value="6">JKUAT</option>
            <option value="7">Kabarak</option>
            <option value="8">KCA</option>
            <option value="9">KEMU</option>
            <option value="10">KU</option>
            <option value="11">Maseno</option>
            <option value="12">Masinde Muliro</option>
            <option value="13">Moi</option>
            <option value="14">Strathmore</option>
            <option value="15">UoN</option>
            <option value="16">USIU</option>
     </select><br/>
 </div>
 <div>
   <label for="author">article by:</label>
   <input type="text" name="author" id="author" value="%s" readonly /><br/>
 </div>
 <div>
   <label for="latitude">latitude:</label>
   <input type="text" name="latitude" id="latitude" value="0.0" readonly /><br/>
 </div>
 <div>
   <label for="longitude">longitude:</label>
   <input type="text" name="longitude" id="longitude" value="0.0" readonly /><br/>
 </div>
 <input type="submit" value="post" data-inline="true" data-theme="d"/>
</form>
</div>'''%(" "+user.nickname()+" : "+user.email())
         footer = '''<div data-role="footer" data-theme="a"> 
			<div class="footertext"> 
			&copy CampusDaily
			</div> 
		   </div> 
		</div> 
	</body> 
</html>'''
         self.response.out.write(header+content+footer)
   def post(self):
      image = images.resize(self.request.get('image'),320,240)
      content = self.request.get('content')
      category = self.request.get('category')
      campustag = self.request.get('campustag')
      latitude = self.request.get('latitude')
      longitude = self.request.get('longitude')
      author = self.request.get('author')
      if image == '' or content == '' or category == '' or campustag == '' or author == '':
        self.redirect('/breaknews')
      else:
         articleprimaryid = ''
         #get last primaryid ...
         query = Articlestable.all()
         query.order('-timestamp') #order by timestamp desc ... most recent to least recent ...
         queryresults = query.fetch(1,0)
         if not queryresults:
            articleprimaryid = '1'
         else:
            for article in queryresults:
               articleprimaryid = str(int(article.primaryid)+1)
         #upload article and details to datastore ...
         article = Articlestable()
         article.primaryid = articleprimaryid
         article.image = db.Blob(image)
         article.content = content
         article.category = category
         article.campustag = campustag
         article.author = author
         article.latitude = latitude
         article.longitude = longitude
         article.timestamp = int(time.time())
         article.views = '2'
         article.put()
         if category == 'general news':self.redirect('/newspage')
         elif category == 'events':self.redirect('/eventspage')
         elif category == 'sports':self.redirect('/sportspage')
         else:self.redirect('/politicspage')
#end class Breaknewspage ...

