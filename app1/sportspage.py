from google.appengine.ext import webapp
from database import * #need this module to populate datastore ...
import timestamper #contains timestamper def to get time of article post ...

class Sportspage(webapp.RequestHandler):
   def get(self):
      offset = self.request.get('offset')
      if offset == '':
         offset = 0
      else:
         offset = int(offset)
      content = ''
      query = Articlestable.all()
      query.filter('category','sports')
      query.order('-timestamp') #order by timestamp desc ... most recent to least recent ...
      queryresults = query.fetch(10,offset)
      if not queryresults:
         content = '<div class="content" data-role="content" data-theme="a"><br/><br/><br/><br/><br/><br/>sorry no articles found<br/><br/><br/><br/><br/><br/></div>'
      else:
         for article in queryresults:
            articlecontent = '''<div class="newsarticlesummaryimageblock"><img class="newsarticlesummaryimage" alt="image" src="/image?imageid=%s" width=80 /></div>
		<div class="newsarticlesummarytextblock">%s<a class="newsarticlesummarytimestamp" href="/getarticle?articleid=%s"><br/>read more ...</a><br/><br/><div class="newsarticlesummarytimestamp">%s, <b>%s</b> views,<br/> article by <b>%s</b></div></div>
		<div class="newsarticlesummaryendline"></div>'''%(article.key(),article.content[:300],article.key(),timestamper.timestamper(article.timestamp),article.views,article.author)
            content = content + articlecontent
         morearticleslink = ''
         queryresults = query.fetch(10,offset+10)
         if queryresults:
            morearticleslink = '<div><a class="newsarticlesummarytimestamp" href="/newspage?offset=%d"><br/>more articles...</a></div>'%(offset+10)
         #create content ...
         content = '<div class="content" data-role="content" data-theme="a">' + content + morearticleslink + '</div>'
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
			CampusDaily
		</title> 
	</head> 
	<body>
		<div data-role="page"> 
			<div data-role="header" data-theme="a">
                                <div class="headertext"> 
				CampusDaily
				</div>
                        </div>'''
      footer = '''
                <ul data-role="listview" data-inset="false" data-theme="a">
                    <li><a href="/newspage">general news</a></li>
		    <li><a href="/eventspage">events</a></li>
		    <li><a href="/sportspage">sports</a></li>
		    <li><a href="/politicspage">politics</a></li>
                    <li><a href="/">home</a></li>
                </ul>
		<div data-role="footer" data-theme="a"> 
			<div class="footertext"> 
			&copy CampusDaily
			</div> 
		</div> 
		</div> 
	</body> 
</html>'''
      self.response.out.write(header+content+footer)
#end class Sportspage ...
