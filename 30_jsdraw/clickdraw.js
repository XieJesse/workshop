var c = document.getElementById('slate') ;

var ctx = c.getContext("2d") ;

var mode = "rect" ;

var toggleMode = (e) => {
  console.log("toggling...") ;
  if (mode === "rect") {
    mode = "circ" ;
  }
  else {
    mode = "rect" ;
  }
} ;

var drawRect = function(e) {
  var mouseX = e.offsetX ;
  var mouseY = e.offsetY ;
  console.log("mouseclick registered at ",mouseX, mouseY)
  ctx.beginPath() ;
  ctx.rect(mouseX, mouseY, 75, 150);
  ctx.fillStyle = 'red'  ;
  ctx.strokeStyle = 'red'  ;
  ctx.stroke();
  ctx.fill();
}

var drawCircle = (e) => {
  var mouseX = e.offsetX ;
  var mouseY = e.offsetY ;
  ctx.beginPath() ;
  ctx.arc(mouseX,mouseY,40,0, 2 * Math.PI) ;
  ctx.fillStyle = 'red' ;
  ctx.fill();
  console.log("mouseclick register at ", mouseX, mouseY) ;
} ;

var draw = (e) => {
  if (mode === "rect") {
    drawRect(e) ;
  }
  else {
    drawCircle(e) ;
  }
}

var wipeCanvas = function() {
  ctx.clearRect(0, 0, c.clientWidth, c.clientHeight);
} ;

c.addEventListener("click", draw);
var toggler = document.getElementById("buttonToggle");
toggler.addEventListener('click',toggleMode) ;
var clear = document.getElementById("buttonClear");
clear.addEventListener('click',wipeCanvas) ;
