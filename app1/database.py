from google.appengine.ext import db

class Articlestable(db.Model):
   primaryid = db.StringProperty()
   image = db.BlobProperty()
   content = db.TextProperty()
   category = db.StringProperty()
   campustag = db.StringProperty()
   author = db.StringProperty()
   latitude = db.StringProperty()
   longitude = db.StringProperty()
   timestamp = db.IntegerProperty()
   views = db.StringProperty()
#end class Articlestable ...
