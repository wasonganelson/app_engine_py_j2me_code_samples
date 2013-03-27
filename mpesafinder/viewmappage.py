from google.appengine.ext import webapp
from database import * #need this module to populate datastore ...
import calculatedistance #contains calculatedistance ...

class Viewmappage(webapp.RequestHandler):
   def get(self):
      offset = self.request.get('offset')
      userlatitude = float(self.request.get('userlatitude'))
      userlongitude = float(self.request.get('userlongitude'))
      agentatmlatitude = float(self.request.get('agentatmlatitude'))
      agentatmlongitude = float(self.request.get('agentatmlongitude'))
      header = '''<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
    <link type="text/css" rel="stylesheet" href="jscss/style.css" />
    <style type="text/css">
      html { height: 100% }
      body { height: 100%; margin: 0; padding: 0 }
      #map_canvas { height: 100% }
    </style>
    <script type="text/javascript"
      src="http://maps.googleapis.com/maps/api/js?key=AIzaSyB0ac81tEAGDJxZaOTlnj4&sensor=false">
    </script>
    <script type="text/javascript">
      var directionsDisplay;
var directionsService = new google.maps.DirectionsService();
var map;
var user = new google.maps.LatLng('''+ str(userlatitude)+''','''+ str(userlongitude)+''');
var agentatm = new google.maps.LatLng('''+ str(agentatmlatitude)+''','''+ str(agentatmlongitude)+''');
//var user = new google.maps.LatLng(-4.0434771, 39.6883070);
//var agentatm = new google.maps.LatLng(-4.0434771, 39.6582065);

function initialize() {
  directionsDisplay = new google.maps.DirectionsRenderer();
  var mapOptions = {
    zoom: 1,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    center: user
  }
  map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);
  directionsDisplay.setMap(map);
}

function calcRoute() {
  var request = {
      origin: user,
      destination: agentatm,
      // Note that Javascript allows us to access the constant
      // using square brackets and a string value as its
      // "property."
      travelMode: google.maps.TravelMode["WALKING"]
  };
  directionsService.route(request, function(response, status) {
    if (status == google.maps.DirectionsStatus.OK) {
      directionsDisplay.setDirections(response);
    }
  });
}
    </script>
  </head>
  <body onload="window.scrollTo(0, 1);initialize();calcRoute();">
    <div id="map_canvas" style="width:100%; height:100%;"></div>
    <a class="mapbackspana" href="/mpesapointsaround?userlatitude='''+ str(userlatitude)+'''&userlongitude='''+ str(userlongitude)+'''&offset='''+ offset +'''" >
        <button class="mapbackspan"> << back </button>
    </a>
   </div>
  </body>
</html>
                '''
      self.response.out.write(header)
#end class Viewmappage ...
