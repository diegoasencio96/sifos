var registrarTerreno = function(){
    return {
        map : "",
        gestorDibujo: "",
        poligono: null,

        init: function(){
            this.map = new google.maps.Map(document.getElementById('mapsDiv'), {
                center: {lat: 4.1247567, lng: -73.6440795},
                zoom: 8
              });
        },

        dibujarPoligono: function(){            
            if (this.map == undefined || this.map == ""){
                alert("No fue posible obtener información del mapa");
                return;
            }
            $("#borrarPoligonoBtn").show();   
            $("#dibujarPoligonoBtn").hide();
            registrarTerreno.gestorDibujo = new google.maps.drawing.DrawingManager({
                drawingMode: google.maps.drawing.OverlayType.POLYGON,
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

            google.maps.event.addListener(registrarTerreno.gestorDibujo, 'polygoncomplete', function(poligono) {                                
                registrarTerreno.poligono = poligono;
                
                registrarTerreno.dibujarElementosPoligono();             

                registrarTerreno.gestorDibujo.setOptions({
                    drawingControl: false          
                });
                registrarTerreno.gestorDibujo.setDrawingMode(null);

            });
            
            registrarTerreno.gestorDibujo.setMap(this.map);
            
            
        },

        borrarPoligono: function(){
            if (this.poligono != null){
                this.poligono.setMap(null);
                this.poligono = null;
            }
            
            $("#dibujarPoligonoBtn").show();
            $("#borrarPoligonoBtn").hide();
            $("#areaPoligonoLbl").html("");
            $("#perimetroPoligonoLbl").html("");
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
            if (this.poligono == null){                
                alert("Debe seleccionar un polígono que represente el terreno");
                return;
            }
            var nombre = $("#nombreTerrenoTxt").val();
            if(nombre == ""){
                alert("Agregue el nombre del terreno");
                return;
            }
            
            var data = {
                points : registrarTerreno.poligono.getPath().getArray(),
                name : nombre
            };
            
        }
    }
}();

