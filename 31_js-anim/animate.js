var c = document.getElementById('playground') ;
var dotButton = document.getElementById('buttonCircle') ;
var stopButton = document.getElementById('buttonStop') ;

var ctx = c.getContext("2d") ;
ctx.fillStyle = 'green' ;

var requestID ;

var clear = (e) => {
  console.log("clear invoked...")
  ctx.clearRect(0, 0, c.clientWidth, c.clientHeight);
};

var radius = 1 ;
var growing = true ;

var drawDot = () => {
  console.log("drawDot invoked...")
  clear() ;
  ctx.beginPath() ;
  ctx.arc(250,250,radius,0, 2 * Math.PI) ;
  ctx.fill() ;
  if (growing) {
    radius++ ;
  }
  else {
    radius -- ;
  }
  if (radius === 250) {
    growing = false ;
  }
  if (radius === 0) {
    growing = true ;
  }
  window.cancelAnimationFrame(requestID) ;
  requestID = window.requestAnimationFrame(drawDot) ;


}

//var stopIt = function() {
var stopIt = () => {
  console.log("stopIt invoked...")
  console.log( requestID );

  window.cancelAnimationFrame(requestID) ;

};


dotButton.addEventListener('click',drawDot)
stopButton.addEventListener('click',stopIt)
