from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.api import images

class Getimage(webapp.RequestHandler):
   def get(self):
      article = db.get(self.request.get("imageid"))
      if article.image:
         self.response.headers['Content-Type'] = "image/jpeg"
         self.response.out.write(article.image)
      else:
         self.error(404)
#end class Getimage ...
