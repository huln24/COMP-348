; Recursive solution

(defun tribonacci (n)
    (cond ((equal n 0) nil) 
       ((equal n 1) 0)
        ((equal n 2) 0)
        ((equal n 3) 1)
        (t (+ (tribonacci (- n 3)) (tribonacci (- n 2)) (tribonacci (- n 1))))
    )
)

(defun tribonacci-seq (n) 
    (if (equal n 0) nil
    (append (tribonacci-seq (- n 1)) (list(tribonacci n)))
        )
)


(print (tribonacci-seq 7))
(print (tribonacci-seq 0))
(print (tribonacci-seq 1))