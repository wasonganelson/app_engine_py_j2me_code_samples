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

$('#breaknewspage').live('pageshow',function(event, ui)
{
    navigator.geolocation.getCurrentPosition(getlocation, function error()
    {
        alert("Error obtaining your location, please refresh the page else default values will be used");
        document.getElementById("latitude").value = "-4.0400224";
        document.getElementById("longitude").value = "39.6570464";
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

function getnewsaroundme()
{
  navigator.geolocation.getCurrentPosition(getlocation1, function error()
    {
        alert("Error obtaining your location, default location values used");
        window.location = "/newsaroundme?userlatitude=-4.0400224&userlongitude=39.6570464"
    },
    {enableHighAccuracy:true});
}

function getlocation1(position)
{
  var latitude = position.coords.latitude;
  var longitude = position.coords.longitude;
  window.location = "/newsaroundme?userlatitude="+latitude+"&userlongitude="+longitude
}
