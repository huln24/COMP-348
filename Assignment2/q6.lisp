; Depth of an atom is 0
; Depth of a list with no inner list 1
; Depth of a list with inner list, max depth among all innner elements plus 1

(defun depth (lst)
    (if (atom lst) 0
        (+ 1 (apply #'max (mapcar #'depth lst)))
    )
)

(print (depth NIL)) ; 0
(print (depth 1))   ; 0
(print (depth '(1))) ;1
(print (depth '((2)) )) ;2
(print (depth '( (2) (3 (6)) (4) )))  ;3
(print (depth '(1(2(3(4(5)))))))  ;5


