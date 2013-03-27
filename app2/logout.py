from google.appengine.api import users
from google.appengine.ext import webapp
from database import * #need this module to populate datastore ...

class Logout(webapp.RequestHandler):
   def get(self):
      user = users.get_current_user()
      if user:
         self.redirect(users.create_logout_url("/"))
      else:
         self.redirect(users.create_logout_url("/"))
#end class Logout ...
