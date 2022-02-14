var c = document.getElementById("canvas") ;

var ctx = c.getContext("2d") ;

var mode = "rect" ;

var toggleMode = (e) => {
  console.log("toggling...") ;
  if (mode == "rect") {
    mode = "circ" ;
  }
  else {
    mode == "rect" ;
  }
} ;

var drawRect = function(e) {
  var mouseX = offsetX ;
  var mouseY = offsetY ;
  console.log("mouseclick registered at ",mouseX, mouseY)
  fillStyle(#ff0000) ;
  strokeStyle(#ff0000) ;
  beginPath() ;
}

var drawCircle = (e) => {
  var mouseX = offsetX ;
  var mouseY = offsetY ;
  arc(mouseX,mouseY,10,0, 2 * Math.PI) ;
  fillStyle(#ff0000) ;
  fill();
  console.log("mouseclick register at ", mouseX, mouseY) ;
}

var wipeCanvas = function() {
  clearRect() ;
} ;
