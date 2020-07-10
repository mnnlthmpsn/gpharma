var gmap

function initMap () {
  var root = document.getElementById('map')

  // get user's position
  navigator.geolocation.getCurrentPosition(pos => {
    lng = -pos.coords.longitude
    lat = pos.coords.latitude

    var map = new google.maps.Map(root, { zoom: 13, center: { lat, lng } })
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
  let glat, glng
  glat = parseFloat(lat)
  glng = -parseFloat(lng)

  var myLatlng = new google.maps.LatLng(glat, glng);

  var pharmloc = new google.maps.Marker({
    position: myLatlng,
    map: gmap
  })
}

function getMap(map) {
  gmap = map
}