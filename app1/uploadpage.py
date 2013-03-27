from google.appengine.ext import webapp
from google.appengine.api import images
from database import * #need this module to populate datastore ...
import time #need this for timestamping ...

class Upload(webapp.RequestHandler):
   def get(self):
      content = '''<html>
            <body>
              <form action="/upload" method="post" enctype="multipart/form-data">
                <label for="image">image:</label>
                <input type="file" name="image" id="image" /><br/>
                <label for="content">content:<br/></label>
                <textarea cols="40" rows="8" name="content" id="content"></textarea><br/>
                <label for="category">category:</label>
                <input type="text" name="category" id="category" value=""/><br/>
                <label for="campustag">campustag: 1-16</label>
                <input type="text" name="campustag" id="campustag" value=""/><br/>
                <label for="author">author:</label>
                <input type="text" name="author" id="author" value=""/><br/>
                <input type="password" name="password" id="password" value=""/><br/>
                <input type="submit" name="submit" value="Submit" />
              </form>
            </body>
          </html>'''
      self.response.out.write(content+'<label><br/><br/> '+self.request.get('message')+'</label>')
   def post(self):
      if self.request.get('password') != '#':#not teargas ...
         self.redirect('/upload?message=fala wewe gotcha...')
      else:#its teargas ...
         image = images.resize(self.request.get('image'),320,240)
         content = self.request.get('content')
         category = self.request.get('category')
         campustag = self.request.get('campustag')
         author = self.request.get('author')
         #upload article and details to datastore ...
         article = Articlestable()
         article.image = db.Blob(image)
         article.content = content
         article.category = category
         article.campustag = campustag
         article.author = author
         article.timestamp = int(time.time())
         article.views = '2'
         article.put()
         self.redirect('/upload?message=      article uploaded...')
#end class Upload ...

