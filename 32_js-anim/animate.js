// Team Grape Surgeons -- Cameron Nelson, Jesse Xie
// SoftDev pd2
// K32 -- canvas based JS animation
// 2022-02-17

// model for HTML5 canvas-based animation

// SKEELTON


//access canvas and buttons via DOM
var c = document.getElementById("playground"); // GET CANVAS
var dotButton = document.getElementById("buttonCircle"); // GET DOT BUTTON
var dvdButton = document.getElementById("buttonDVD");
var stopButton = document.getElementById("buttonStop"); // GET STOP BUTTON

	//prepare to interact with canvas in 2D
var ctx = c.getContext('2d'); // YOUR CODE HERE

	//set fill color to team color
ctx.fillStyle = 'blue'; // YOUR CODE HERE

var requestID = false;  //init global var for use with animation frames


//var clear = function(e) {
var clear = (e) => {
	//console.log("clear invoked...")
	ctx.clearRect(0, 0, c.clientWidth, c.clientHeight);
	// YOUR CODE HERE
};

var circle_radius = 0;
var circle_growing = true;

var drawCircle = () => {
	clear();

	ctx.fillStyle = 'blue';
	ctx.beginPath();
	ctx.arc(c.clientWidth / 2, c.clientHeight / 2, circle_radius, 0,  2 * Math.PI);
	ctx.fill();
	if (circle_growing) {
		if (++circle_radius == Math.min(c.clientWidth / 2,c.clientHeight / 2)) {
			circle_growing = false;
		}
	} else {
		if (--circle_radius == 0) {
			circle_growing = true;
		}
	}

	requestID = window.requestAnimationFrame(drawCircle);
}

//var drawDot = function() {
var drawDot = () => {
	console.log("drawDot invoked...")

	window.cancelAnimationFrame(requestID);
	requestID = window.requestAnimationFrame(drawCircle);
	/*
      ...to
      Wipe the canvas,
      Repaint the circle,
      ...and somewhere (where/when is the right time?)
      Update requestID to propagate the animation.
      You will need
      window.cancelAnimationFrame()
      window.requestAnimationFrame()
	*/
};

var dvd_image = new Image(60,40);
dvd_image.src = "logo_dvd.jpg";

var dvd_x;
var dvd_y;
var dvd_xvel;
var dvd_yvel;

var drawDVD = () => {
	clear();
	//console.log('x: ' + dvd_x + ' y: ' + dvd_y);
	ctx.drawImage(dvd_image, dvd_x, dvd_y, dvd_image.width, dvd_image.height);

	dvd_x += dvd_xvel;
	if (dvd_x <= 0 || dvd_x >= c.clientWidth - dvd_image.width) {
		dvd_xvel *= -1;
	}
	dvd_y += dvd_yvel;
	if (dvd_y <= 0 || dvd_y >= c.clientHeight - dvd_image.height) {
		dvd_yvel *= -1;
	}

	requestID = window.requestAnimationFrame(drawDVD);
}

var startDVD = () => {
	dvd_x = 100 + Math.floor(Math.random() * 301);
	dvd_y = 100 + Math.floor(Math.random() * 301);
	/*
	let temp = Math.floor(Math.random() * 4);
	dvd_xvel = 2 * (temp % 2) - 1;
	dvd_yvel = (temp >= 2) ? 1 : -1;
	*/
	dvd_xvel = 1;
	dvd_yvel = 1;

	window.cancelAnimationFrame(requestID);
	requestID = window.requestAnimationFrame(drawDVD);
}

//var stopIt = function() {
var stopIt = () => {
	console.log("stopIt invoked...")
	console.log( requestID );

	window.cancelAnimationFrame(requestID);
	requestID = false;
	// YOUR CODE HERE
	/*
      ...to
      Stop the animation
      You will need
      window.cancelAnimationFrame()
	*/
};

dotButton.addEventListener( "click", drawDot );
dvdButton.addEventListener( "click", startDVD);
stopButton.addEventListener( "click",  stopIt );
