// Team Will Smith:: Jesse Xie, Angela Zhang
// SoftDev pd0
// K27 -- Basic functions in JavaScript
// 2022-02-04
// --------------------------------------------------


var fib = function(n) {
  if(n <= 1) return n ;
  else return (fib(n-1) + fib(n-2)) ;
};

var fac = function(n) {
  if(n == 1) return 1 ;
  else return (n * fac(n-1)) ;
};
