

$(document).ready(function() {

$('#query').keyup(function(e) {    
   if(e.keyCode == 13) {
     
         function showLoading() {
             $("#loading").show();
         }

         function hideLoading() {
             $("#loading").hide();
         }

         showLoading();

       $.ajax({
          data : {
             query : $('#query').val(),
             
                 },
             type : 'POST',
             url : '/process'
            })
          .done(function(data) {
              $('#output').text(data.output).show();
              $('#wikipedia').text(data.wiki).show();
              $('#adress').text(data.adress).show();
         
              $('#output').addClass('one');
              $('#wikipedia').addClass('one');
              $('#adress').addClass('one');
              $('#wikipedia_1').attr({href:data.url,target:'_blank'});
              $('#wikipedia_1').text(data.url).show()
              latitude = data.lat;
              longitude = data.lng;
              place_id = data.place_id;
              wiki = data.wiki;
              adress = data.adress;
              url = data.url;
              adress_2 = data.adress_2
              console.log(latitude)
              console.log(longitude)
              console.log(place_id)
              console.log(wiki)
              console.log(adress)
              console.log(url)
              console.log(adress_2)

              function initMap() {
                // New map
        
                var map = new google.maps.Map(document.getElementById('map'), {
                   center: {lat: latitude, lng: longitude},
                   zoom: 15
                                });

                var request = {

                  placeId: place_id,
                  fields: ['name', 'formatted_address', 'place_id', 'geometry']
                              };

                var infowindow = new google.maps.InfoWindow();
                var service = new google.maps.places.PlacesService(map);

                service.getDetails(request, function(place, status) {
                   if (status === google.maps.places.PlacesServiceStatus.OK) {
                       var marker = new google.maps.Marker({
                          map: map,
                          position: {lat: latitude, lng: longitude}
                    });
                google.maps.event.addListener(marker, 'click', function() {
                    infowindow.setContent('<div><strong>' + place.name + '</strong><br>' +
                    'Place ID: ' + place.place_id + '<br>' +
                    place.formatted_address + '</div>');
                    infowindow.open(map, this);
                    });
                }
             });
          }

           initMap();
           hideLoading();
       
        })
        
      
      }
    });

});
