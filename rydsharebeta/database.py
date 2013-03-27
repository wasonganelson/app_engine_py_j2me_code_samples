from google.appengine.ext import db

class Userstable(db.Model):
   timestamp = db.IntegerProperty()
   aaprimaryid = db.IntegerProperty()
   useremail = db.StringProperty()
   username = db.StringProperty()
   userphonenumber = db.StringProperty()
   userpreferences = db.TextProperty()
   userprofileimage = db.BlobProperty()
#end class Userstable ...

class Ridessharedtable(db.Model):
   timestamp = db.IntegerProperty()
   aaprimaryid = db.IntegerProperty()
   useremail = db.StringProperty()
   departurepoint = db.StringProperty()
   destinationpoint = db.StringProperty()
   departuretime = db.IntegerProperty()
   seatsavailable = db.IntegerProperty()
   costperseat = db.IntegerProperty()
   latitude = db.StringProperty()
   longitude = db.StringProperty()
   status = db.StringProperty()
#end class Rideposttable ...

class Liftseekerstable(db.Model):
   timestamp = db.IntegerProperty()
   aaprimaryid = db.IntegerProperty()
   useremail = db.StringProperty()
   departurepoint = db.StringProperty()
   destinationpoint = db.StringProperty()
   departuretime = db.IntegerProperty()
   costperseat = db.IntegerProperty()
   latitude = db.StringProperty()
   longitude = db.StringProperty()
   status = db.StringProperty()
#end class Seeklifttable ...

class Usersnetworktable(db.Model):
   aaprimaryid = db.IntegerProperty()
   useremail = db.StringProperty()
   usernetwork = db.TextProperty()
   usernetworkrq = db.TextProperty()
#end class Usersnetworktable ...
