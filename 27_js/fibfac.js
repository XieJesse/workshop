// Team Will Smith:: Jesse Xie, Angela Zhang
// SoftDev pd0
// K27 -- Basic functions in JavaScript
// 2022-02-04
// --------------------------------------------------


var fib = function(args) {
  if(args <= 1) return args ;
  else return (fib(args-1) + fib(args-2)) ;
};
