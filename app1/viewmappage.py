from google.appengine.ext import webapp
from database import * #need this module to populate datastore ...
import timestamper #contains timestamper def to get time of article post ...
import calculatedistance #contains calculatedistance ...

class Viewmappage(webapp.RequestHandler):
   def get(self):
      articlelatitude = float(self.request.get('articlelatitude'))
      articlelongitude = float(self.request.get('articlelongitude'))
      header = '''<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
    <style type="text/css">
      html { height: 100% }
      body { height: 100%; margin: 0; padding: 0 }
      #map_canvas { height: 100% }
    </style>
    <script type="text/javascript"
      src="http://maps.googleapis.com/maps/api/js?key=AIzaSyB0axZaOXnKYVgbhgSthTlnj4&sensor=false">
    </script>
    <script type="text/javascript">
      function initialize() {
        window.scrollTo(0, 1);
        var myLatlng = new google.maps.LatLng( '''+ str(articlelatitude) +''', '''+ str(articlelongitude) +''');
        var mapOptions = {
          center: myLatlng,
          zoom: 16,
          mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        var map = new google.maps.Map(document.getElementById("map_canvas"),
            mapOptions);
        var marker = new google.maps.Marker({
        position: myLatlng,
        map: map,
        title:"over here"
                            });
      }
    </script>
  </head>
  <body onload="initialize()">
    <div id="map_canvas" style="width:100%; height:100%"></div>
  </body>
</html>
                '''
      self.response.out.write(header)
#end class Viewmappage ...
