; Iterative solution

(defun tribonacci-seq (n)
    (defparameter lst '())   ; List of tribonacci sequence to be returned 
    (defparameter x 0)
    (defparameter y 0)
    (defparameter z 1)
    (cond ((equal n 0) nil)
        ((equal n 1) x)
        ((equal n 2) (list x y))
        ((equal n 3) (list x y z))
        (t
            (let ((i 4) (lst (list x y z)))
                (loop 
                    (when (> i n) (return lst))
                    (setf lst (append lst (list (+ x y z))))
                    (setf sum (+ x y z))
                    (setf x y)
                    (setf y z)
                    (setf z sum)
                    (incf i)
                )      
            )
        )     
    )
)  

(print (tribonacci-seq 8))
(print (tribonacci-seq 0))
(print (tribonacci-seq 1))