from google.appengine.ext import webapp

class Error(webapp.RequestHandler):
   def get(self):
      header = '''
<!DOCTYPE html>
<link type="text/css" rel="stylesheet" href="jscss/style.css" />
<body>
	<div class="pageheader">CampusDaily</div>'''
      content = '''
<div class="pagecontent">
          <div class="aboutcontent"><br/><br/><br/><br/>Error ! Use your android, iphone or ipod-touch browser to access this webservice ...<br/><br/><br/><br/></div>
        </div>'''
      footer = '''<div class="pagefooter">&copy CampusDaily</div>
</body>
</html>'''
      self.response.out.write(content)
#end class Error ...
