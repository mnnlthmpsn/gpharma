var gmap
var userLoc
var pharmaLoc
var directS
var directD


function initMap () {
  var root = document.getElementById('map')
  var directionsService = new google.maps.DirectionsService();
  var directionsDisplay = new google.maps.DirectionsRenderer();

  setdirectionService(directionsService)
  setdirectionDisplay(directionsDisplay)
  // get user's position
  navigator.geolocation.getCurrentPosition(pos => {
    lng = pos.coords.longitude
    lat = pos.coords.latitude

    var map = new google.maps.Map(root, { zoom: 13, center: { lat, lng } })
    getMap(map)
    var user = new google.maps.LatLng(parseFloat(lat), parseFloat(lng))
    setUser(user)
  })
}


// get pharmacy location
function getpharmloc(lat, lng){
  let glat, glng
  glat = parseFloat(lat)
  glng = parseFloat(lng)

  var myLatlng = new google.maps.LatLng(glat, glng);
  setPharma(myLatlng)
  calcDistance(directS, directD)
}

function getMap(map) {
  gmap = map
}

function setUser(user){
  userLoc = user
}

function setPharma(pharma){
  pharmaLoc = pharma
}

function setdirectionDisplay(directionsDisplay) {
  directD = directionsDisplay
}

function setdirectionService(directionsService) {
  directS = directionsService
}

const calcDistance = (directS, directD) => {
  directD.setMap(gmap)
  directS.route({
    origin: userLoc, 
    destination: pharmaLoc,
    travelMode: google.maps.TravelMode.DRIVING
  }, function(response, status) {
    if (status === 'OK'){
      directD.setDirections(response);
    }
    else {
      window.alert(`Directions request failed due to ${status}`)
    }
  })
}