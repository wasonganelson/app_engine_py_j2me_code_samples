from google.appengine.api import users
from google.appengine.ext import webapp
from database import * #need this module to populate datastore ...

class Login(webapp.RequestHandler):
   def get(self):
      user = users.get_current_user()
      if not user:
         self.redirect(users.create_login_url(self.request.uri))
      else:
         #check that user is not in blacklist ...
         useremail = user.email()
         query = Blacklisttable.all()
         query.filter('useremail',useremail)
         queryresults = query.fetch(1,0)
         if queryresults:# if in blacklist, redirect to blacklist page ...
            self.redirect("/blacklist")
         else:
            #check that user is signed up ...
            query= Userstable.all()
            query.filter('useremail',useremail)
            queryresults = query.fetch(1,0)
            if queryresults:#if signed up, login user ...
               self.redirect("/needitslogin")
            else:#redirect user to sign up page ...
               self.redirect("/signuplogin")
#end class Login ...
