
(defun is-bst (lst)
    (defparameter root (car lst))
    (defparameter left (car (cdr lst)))
    (defparameter right (cdr (cdr lst)))
    (cond 
        ((null root) t)
        ((or (null right) (null left)) t)
        ((not (null left))
             (cond 
                 ((>= (car left) root) nil)
                 ((not (is-bst left)) nil)
                 (t)
              )
         )
        ((not (null right))
             (cond 
                 ((<= (show (car right)) root) nil)
                 ((not (is-bst right)) nil)
                 (t)
             )
        )
        
        (t)
    )
)

(print (is-bst '(30 () (40 () ()))))
(print (is-bst '(8 (3 (1 () ()) (6 (4 () ())(7 () ()))) (10 () (14 (13 () ()) ())))))
(print (is-bst '()))
(print (is-bst '(2 () ())))
(print (is-bst '(30 (20 () ()) ())))
(print (is-bst '(30 (35 () ()) ())))
;(print (is-bst '(30 () (20 () ()))))