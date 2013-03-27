from google.appengine.api import users
from google.appengine.ext import webapp
from database import * #need this module to access datastore ...
import timestamper #contains timestamper def to get time of needit post ...

class Admin(webapp.RequestHandler):
   def get(self):
      #check if user is admin before proceeding ...
      user = users.get_current_user()
      if not user:
         self.redirect(users.create_login_url(self.request.uri))
      elif user.email() != 'needitkenya@gmail.com':
         self.redirect(users.create_login_url(self.request.uri))
      else:
         x = ""
      offset = self.request.get('offset')
      if offset == '':
         offset = 0
      else:
         offset = int(offset)
      content = ''
      query = Needitstable.all()
      query.order('-timestamp') #order by timestamp desc ... most recent to least recent ...
      needits = query.fetch(50,offset)
      if not needits:
         content = '''<div class="pagecontent"><div class="resultsnotfound">sorry no results found ...</div></div>'''
      else:
         for needit in needits:
            needitkey = needit.key()
            need = needit.need
            urgency = needit.urgency
            offer = str(needit.offer)
            userphonenumber = needit.userphonenumber
            useremail = needit.useremail
            username = needit.username
            timestamp = needit.timestamp
            views = str(needit.views)
            #use email to get user profile image ...
            query1 = Userstable.all()
            query1.filter('useremail',useremail)
            queryresults = query1.fetch(1,0)
            imagekey = ''
            for userdetails in queryresults:
               imagekey = userdetails.key()
            needitcontent = '''<div class="needitsummaryblock">
                  <img class="myneeditsummaryimage" src="/getimage?key=%s"/>
                  <div class="myneeditsummarytext">
                      <b>need: </b>%s<br/>
                      <b>urgency: </b>%s<br/>
                      <b>offer: </b>%s Ksh<br/>
                      <b>posted: </b>%s<br/>
                      <b>views: </b>%s<br/> 
                      <a class="removeneeditlink" href="/remove?admin=teargas&key=%s">remove</a>
</div>
                </div>
                <div class="needitsummaryendline"></div>'''%(imagekey, need, urgency, offer, timestamper.timestamper(timestamp), views, needitkey)
            content = content + needitcontent
         moreneeditslink = ''
         queryresults = query.fetch(50,offset+50)
         if queryresults:
             moreneeditslink = '<div align="center"><a class="viewmorelink" href="/admin?offset=%d"><br/>more needits<br/><br/></a></div>'%(offset+50)
         logoutlink = '<div align="center"><a class="viewmorelink" href="/logout"><br/>logout admin<br/><br/></a></div>'
         content = '''<div class="pagecontent">''' + content + moreneeditslink + logoutlink + '''</div>'''
      
      header = '''
<!doctype html>
<html>
<meta name="HandheldFriendly" content="true" />
<meta name="viewport" content="width=device-width; initial-scale=1.0; minimum-scale=1.0; maximum-scale=1.0; user-scalable=0;" />
<style type="text/css">
</style>
<link type="text/css" rel="stylesheet" href="jscss/style.css" />
<body>
	<div class="pageheader">admin</div>
        <div class="needitsummaryendline"></div>'''
      
      footer = '''<div class="pagefooter">&copy need-it</div>
</body>
</html>'''
      self.response.out.write(header+content+footer)
#end class Admin ...
