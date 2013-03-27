from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.api import images

class Getimage(webapp.RequestHandler):
   def get(self):
      userdetails = db.get(self.request.get("key"))
      if userdetails.profileimage:
         self.response.headers['Content-Type'] = "image/png"
         self.response.out.write(userdetails.profileimage)
      else:
         self.error(404)
#end class Getimage ...
