// Team Tofu: Jesse Xie, Annabel Zhang, Justin Zou
// SoftDev pd2
// K28 -- Getting more comfortable with the dev console and the DOM
// 2022-02-08
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;

// why do variables need to be assigned for defining functions?
//assign an anonymous fxn to a var, adds 30 to the number and outputs it
var f = function(x) {
  var j=30;
  return j+x;
};

// o looks like a dictionary
//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 15,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          // function can stored in dictionary object, be returned with
          // o[funcName], and a parameter can be passed into it
          func : function(x) {
            return x+30;
          }
        };

// adds new items to the end of the lists with parameter
var addItem = function(text) {
  // document object seems to interact with the html
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};

// removes items by item index
var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};


// gives items that are black/colorless the red class, turning them red
var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    // document elements have a classList that seems to act like lists
    items[i].classList.add('red');
  }
};

// alternates between red and blue when giving items color classes (by odds and evens)
var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

var fib = function(n) {
  if(n <= 1) return n ;
  else return (fib(n-1) + fib(n-2)) ;
};

var fac = function(n) {
  if(n == 1) return 1 ;
  else return (n * fac(n-1)) ;
};

var gcd = function(a,b) {
  if(a < b) return gcd(b,a) ;
  if(a % b == 0) return b ;
  else return gcd(b,a%b) ;
};

addItem("10th-fib is: "+fib(10))
addItem("10 factorial is: "+fac(10))
addItem("gcd of 148 and 196 is: "+gcd(148,196))
stripe()
