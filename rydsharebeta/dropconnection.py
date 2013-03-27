from google.appengine.api import users
from google.appengine.ext import webapp
from database import * #need this module to access datastore ...

class Dropconnection(webapp.RequestHandler):
   def get(self):
      #check if user session is valid before proceeding ...
      useremaila = '' #email of user currently logged in ...
      useremailb = self.request.get('useremailb') #email of user we want to add to network ...
      user = users.get_current_user()
      if not user:
         self.redirect(users.create_login_url(self.request.uri))
      else:
         useremaila = users.get_current_user().email()
      query = Usersnetworktable.all()
      query.filter('useremail',useremaila)# getting useremaila usernetworkrq ...
      queryresults = query.fetch(1,0)
      for userdetails in queryresults:
         userdetails.usernetwork = userdetails.usernetwork.replace(useremailb,' ')
         userdetails.put()
      query = Usersnetworktable.all()
      query.filter('useremail',useremailb)# getting useremailb usernetworkrq ...
      queryresults = query.fetch(1,0)
      for userdetails in queryresults:
         if useremaila in userdetails.usernetwork.split():
            userdetails.usernetwork = userdetails.usernetwork.replace(useremaila,' ')
         userdetails.put()
      self.redirect('/mynetwork')
#end class Dropconnection ...
