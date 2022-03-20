
(defun pre-order (lst)
    (cond
        ((null lst) nil)        ; If list is empty return nil
        (t (if (and (atom (car lst)) (not (equal (car lst) nil)))  ; If head of lst is an atom
            (append (list (car lst)) (pre-order (cdr lst)))        ; Construct a list with head of list and recur on tail of the list
            (append (pre-order (car lst)) (pre-order (cdr lst))))))   ; Else, recur on head of the list and tail of the list and append them 
)

(print "Pre-order traversal")
(print (pre-order '(+ (- (1 () ()) (* (4 () ())(7 () ()))) (/ (7 () ()) (6 () ())))))

(defun in-order (lst)
  (cond
    ((null lst) nil)
    (t (append (in-order (car (cdr lst)))
       (list (car lst))
       (in-order (car (cdr (cdr lst))))))))

(print "In-order traversal")
(print (in-order '(+ (- (1 () ()) (* (4 () ())(7 () ()))) (/ (7 () ()) (6 () ())))))