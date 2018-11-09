var registrarTerreno = function(){

    return {
        map : "",
        gestorDibujo: "",
        poligono: null,

        init: function(){
            this.map = new google.maps.Map(document.getElementById('mapsDiv'), {
                center: {lat: -34.397, lng: 150.644},
                zoom: 8
              });
        },

        dibujarPoligono: function(){
            if (this.map == undefined || this.map == ""){
                alert("No fue posible obtener información del mapa");
                return;
            }

            gestorDibujo = new google.maps.drawing.DrawingManager({
                drawingMode: google.maps.drawing.OverlayType.MARKER,
                drawingControl: true,
                drawingControlOptions: {
                  position: google.maps.ControlPosition.TOP_CENTER,
                  drawingModes: ['polygon']
                },
                circleOptions: {
                  fillColor: '#ffff00',
                  fillOpacity: 1,
                  strokeWeight: 5,
                  clickable: false,
                  editable: true,
                  zIndex: 1
                }
            });

            google.maps.event.addListener(gestorDibujo, 'polygoncomplete', function(poligono) {                                
                registrarTerreno.poligono = poligono;
                $("#borrarPoligonoBtn").show();   
                registrarTerreno.dibujarElementosPoligono();             

                gestorDibujo.setOptions({
                    drawingControl: false
                });
            });
            
            gestorDibujo.setMap(this.map);
            $("#dibujarPoligonoBtn").hide();
            
        },

        borrarPoligono: function(){
            if (this.poligono != null){
                this.poligono.setMap(null);
                this.poligono = null;
            }
            
            $("#dibujarPoligonoBtn").show();
            $("#borrarPoligonoBtn").hide();
        },

        dibujarElementosPoligono: function(){
            if (this.poligono != null){
                var area = google.maps.geometry.spherical.computeArea(this.poligono.getPath());
                var perimetro = google.maps.geometry.spherical.computeLength(this.poligono.getPath());
                $("#areaPoligonoLbl").html(" " + area.toFixed() + " metros cuadrados (?)");
                $("#perimetroPoligonoLbl").html(" " + perimetro.toFixed() + " metros cuadrados (?)");
            }
        },

        registrarPoligono: function(){
            
        }
    }
}();

