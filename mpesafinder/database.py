from google.appengine.ext import db

class Agentatmtable(db.Model):
   primaryid = db.IntegerProperty()
   businessname = db.StringProperty()
   latitude = db.StringProperty()
   longitude = db.StringProperty()
   businesstype = db.StringProperty()
   verified = db.StringProperty()
#end class Agentatmtable ...

