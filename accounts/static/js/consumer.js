var gmap
var pharma

function initMap () {

  var directionsService = new google.maps.DirectionsService;
  var directionsDisplay = new google.maps.DirectionsRenderer;

  var root = document.getElementById('map')

  calculateAndDisplayRoute = (directionsService, directionsDisplay) => {
    directionsService.route({
      origin: marker,
      destination: pharma,
      travelMode: 'WALKING',
    }, (response, status) => {
      status === 'OK' 
        ? directionsDisplay.setDirections(response)
        : window.alert(`Directions request failed due to ${status}`)
    })
  }

  // get user's position
  navigator.geolocation.getCurrentPosition(pos => {
    lng = -pos.coords.longitude
    lat = pos.coords.latitude

    var map = new google.maps.Map(root, { zoom: 13, center: { lat, lng } })
    directionsDisplay.setMap(map)
    getMap(map)
    // user locaiton
    var marker = new google.maps.Marker({
      position: { lat, lng },
      map,
      icon:
        'https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png'
    })
  })
}

// get pharmacy location
function getpharmloc(lat, lng){
  console.log(lat)
  console.log(lng)
  let glat, glng
  glat = parseFloat(lat)
  glng = -parseFloat(lng)

  var myLatlng = new google.maps.LatLng(glat, glng);

  var pharmloc = new google.maps.Marker({
    position: myLatlng,
    map: gmap
  })
  pharma = pharmloc
}

function getMap(map) {
  gmap = map
}