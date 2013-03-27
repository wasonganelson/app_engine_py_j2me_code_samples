from google.appengine.ext import webapp
from database import * #need this module to access datastore ...

class Remove(webapp.RequestHandler):
   def get(self):
      if(self.request.get("admin") == 'teargas'):
         #use key to fetch needit details from datastore and delete ...
         needit = db.get(self.request.get("key"))
         useremail = needit.useremail
         needit.delete()
         #use useremail to remove user from Userstable ...
         query= Userstable.all()
         query.filter('useremail',useremail)
         queryresults = query.fetch(1,0)
         for results in queryresults:results.delete()
         #use useremail to blacklist user ...
         blacklistuser = Blacklisttable()
         blacklistuser.useremail = useremail
         blacklistuser.put()
         self.redirect('/admin')
      else:
         #use key to fetch needit details from datastore and delete ...
         needit = db.get(self.request.get("key"))
         needit.delete()
         self.redirect('/myneeditslogin')
#end class Remove ...
