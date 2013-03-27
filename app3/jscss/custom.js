$(document).bind("mobileinit", function(){
  var ua = navigator.userAgent;
  var checker = {
                 iphone: ua.match(/(iPhone|iPod|iPad)/),
                 blackberry: ua.match(/BlackBerry/),
                 android: ua.match(/Android/)
                };
  if(checker.android || checker.iphone || checker.blackberry)
  {
     $.mobile.ajaxEnabled = false;
     $.mobile.defaultPageTransition = "pop";
  }
  else{window.location = "/error"}
  
 //  $.mobile.ajaxEnabled = false;
 //  $.mobile.defaultPageTransition = "pop";
});
$('div').live('pageshow',function(event, ui){
  window.scrollTo(0, 1);
});

$('#postneeditpage').live('pageshow',function(event, ui)
{
    navigator.geolocation.getCurrentPosition(getlocation, function error()
    {
        alert("Error obtaining your location, please refresh the page else default values will be used");
        document.getElementById("latitude").value = "0.2400224";
        document.getElementById("longitude").value = "34.2770464";
    },
    {enableHighAccuracy:true});
});

function getlocation(position)
{
  var latitude = position.coords.latitude;
  var longitude = position.coords.longitude;
  document.getElementById("latitude").value = latitude;
  document.getElementById("longitude").value = longitude;
}

var url = ""
function getneeditsaroundme()
{
  navigator.geolocation.getCurrentPosition(getlocation1, function error()
    {
        alert("Error obtaining your location, default location values used");
        window.location = url+"?userlatitude=0.2400224&userlongitude=34.2770464"
    },
    {enableHighAccuracy:true});
}

function getlocation1(position)
{
  var latitude = position.coords.latitude;
  var longitude = position.coords.longitude;
  window.location = url+"?userlatitude="+latitude+"&userlongitude="+longitude
}
