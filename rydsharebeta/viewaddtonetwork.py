from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.api import mail
from database import * #need this module to access datastore ...

class Viewaddtonetwork(webapp.RequestHandler):
   def get(self):
      #check if user session is valid before proceeding ...
      imagekey = ''
      useremaila = '' #email of user currently logged in ...
      useremailb = self.request.get('email') #email of user we want to add to network ...
      username = ''
      userphonenumber = ''
      userpreference = ''
      usernetwork = ''
      button = ''
      user = users.get_current_user()
      if not user:
         self.redirect(users.create_login_url(self.request.uri))
      else:
         useremaila = users.get_current_user().email()
      query = Userstable.all()
      query.filter('useremail',useremailb) #getting details of user we want to add to network ...
      queryresults = query.fetch(1,0)
      for userdetails in queryresults:
         imagekey = userdetails.key()
         username = userdetails.username
         userpreferences = userdetails.userpreferences
         userphonenumber = userdetails.userphonenumber
      query = Usersnetworktable.all()
      query.filter('useremail',useremailb)
      queryresults = query.fetch(1,0)
      for userdetails in queryresults:
         usernetworkrq = userdetails.usernetworkrq
      usernetworkrq = usernetworkrq.split()
      if useremaila in usernetworkrq:
         button = '<div align="center"><b>connection request sent</b><br/></div>'
      else:
         button = '<input class="button" type="submit" value="send request"/><br/>'
         
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
			Rideshare-Ke
		</title> 
	</head> 
	<body>
		<div data-role="page" data-theme="a"> 
			<div data-role="header" data-theme="a">
				<h3>Rideshare-Ke</h3>
			</div>'''

      content = '''
<div data-role="content" data-theme="a">
            <div class="signupcontent">
              <img class="ridesharekenyaprofileimage" alt="upload image" src="/getimage?key=%s"/><br/><br/>
              <div class="ridesharekenyaprofiletext">
                 <b>email:</b> %s<br/><br/>
              </div>
              <form method="post" action="/viewaddtonetwork" enctype="multipart/form-data">
                <label for="username"><b>username:</b> %s</label><br/><br/>
                <label for="userphonenumber"><b>tel no:</b> %s</label><br/><br/>
                <label for="userpreferences"><b>user preferences:</b> %s</label><br/><br/>
                <input type="hidden" name="useremailb" id="useremailb" value="%s"/>
                %s
              </form>
            </div>
        </div>''' % (imagekey, useremailb, username, userphonenumber, userpreferences, useremailb, button)

      footer = '''
<ul data-role="listview" data-inset="false" data-theme="a"> 
	<li>
		<a onclick="url='/ridessharedaroundme';getridessharedaroundme();"> 
			rides shared
		</a> 
	</li>
        <li> 
		<a onclick="url='/liftseekersaroundme';getliftseekersaroundme();"> 
			lift seekers
		</a> 
	</li>
        <li> 
		<a href="/postridelogin"> 
			share ride
		</a> 
	</li>
        <li> 
		<a href="/seekliftlogin"> 
			seek lift
		</a> 
	</li>
        <li> 
		<a href="/aboutlogin"> 
			about
		</a> 
	</li>
        <li> 
		<a href="/helplogin"> 
			help
		</a> 
	</li>
        <li> 
		<a href="/logout"> 
			log out
		</a> 
	</li>
</ul>
<div data-role="navbar" data-theme="a">
	<ul><li><a href="/ridesharekenyalogin">main<br/>menu</a></li>
	<li><a href="/myaccount">my<br/>account</a></li>
	<li><a href="/mynetwork">my<br/>network</a></li>
	<li><a href="/addtonetwork">add to<br/>network</a></li></ul>
</div>
<div data-role="footer" data-theme="a"> 
			<h6 class="footertext">&copy Rideshare-Ke</h6>
		</div>
</body>
</html>'''
      self.response.out.write(header+content+footer)

   def post(self):
      #check if user session is valid before proceeding ...
      useremaila = ''
      useremailaname = ''
      useremailb = self.request.get('useremailb')
      user = users.get_current_user()
      if not user:
         self.redirect(users.create_login_url(self.request.uri))
      else:
         useremaila = users.get_current_user().email()
      query = Usersnetworktable.all()
      query.filter('useremail',useremailb) #getting useremailb usernetwork ...
      queryresults = query.fetch(1,0)
      for userdetails in queryresults:
         userdetails.usernetworkrq += ' '+useremaila
         userdetails.put()
      query = Userstable.all()
      query.filter('useremail',useremaila) #getting useremaila username ...
      queryresults = query.fetch(1,0)
      for userdetails in queryresults:
         useremailaname = userdetails.username
      #send mail notification of request ...
      message = '%s (%s) sent you a connection request on ridesharekenya. ' % (useremailaname, useremaila)
      mail.send_mail('ridesharekenya@gmail.com', useremailb, 'Rideshare Connection Request', message)
      self.redirect('/viewaddtonetwork?email='+useremailb)
#end class Viewaddtonetwork ...
