from google.appengine.ext import webapp
from database import * #contains Model classes that will be used for creating a datastore ...
import timestamper #contains timestamper def to get time of article post ...

class Getarticlepage(webapp.RequestHandler):
   def get(self):
      article = db.get(self.request.get("articleid"))
      #update article views ...
      article.views = str(int(article.views)+1)
      article.put()
      content = ''
      content = content + '''<div class="newsarticleimageblock" align="center"><img class="newsarticleimage" alt="image" src="/image?imageid=%s" /></div><div class="newsarticletextblock">%s<br/><br/><div class="newsarticlesummarytimestamp">article posted %s, <b>%s</b> views</div><br/><span class="authortag">by <b>%s</b></span><br/></div>
		<div class="newsarticlesummaryendline"></div></div>'''%(article.key(),article.content,timestamper.timestamper(article.timestamp),article.views,article.author)
      #create content ...
      content = '<div class="content" data-role="content" data-theme="a">' + content + '''<div class="facebookcomments">
                      <br/><div class="fb-like" data-href="%s" data-send="false" data-width="1" data-show-faces="true">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div>
<div>
<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a data-count="horizontal" data-text="%s" data-counturl="%s" href="%s" class="twitter-share-button" data-lang="en">Tweet</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
</div>
                      <br/><br/><div class="fb-comments" data-href="%s" data-width="320" data-num-posts="10"></div>
                    </div>'''%(self.request.uri, " ",self.request.uri,self.request.uri,self.request.uri)
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
                <div id="fb"><div id="fb-root"></div>
                              <script>(function(d, s, id) {
                              var js, fjs = d.getElementsByTagName(s)[0];
                              if (d.getElementById(id)) return;
                              js = d.createElement(s); js.id = id;
                              js.src = "//connect.facebook.net/en_US/all.js#xfbml=1&appId=213774082058077";
                              fjs.parentNode.insertBefore(js, fjs);
                              }(document, 'script', 'facebook-jssdk'));</script>
                </div>
		<div data-role="page"> 
			<div data-role="header" data-theme="a">
                                <div class="headertext"> 
				CampusDaily
				</div>
                        </div>'''
      footer = '''
                <ul data-role="listview" data-inset="false" data-theme="a">
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
#end class Getarticlepage ...
