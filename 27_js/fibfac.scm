;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname fibfac) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(define fib
  (lambda (n)
    (if (<= n 1)
	n
        (+ (fib(- n 1)) (fib(- n 2)))
     )
        
   )
 )
  
(define fact
    (lambda (n)
        (if (= n 0)
            1
            (* (fact(- n 1)) n)
        )
    )
)
