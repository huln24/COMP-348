; Auxiliary recursive function to get the sub list

(defun get-sub (sublst from to i)
    (if (= i to) (cons (car sublst) nil)
        (cond ((< i from) (get-sub (cdr sublst) from to (+ i 1)))     ; Before reaching from index, ignore head of the list
              ((>= i from) (cons (car sublst) (get-sub (cdr sublst) from to (+ i 1)))) 
              ; After reaching from index, construct a list with head of list and recursion of the tail
        )
    )
) 


(defun sub-list2 (lst from &optional (to nil))
    (if (or (equal to nil) (> to (list-length lst)) (< to 1)) (defparameter to (list-length lst) ())) ; If to index not given or out of bound, use list length as default value 
    (if (< from 1) (defparameter from 1) ())        ; If from index is out ouf bound, use 1 as default value
    (cond ((null lst) nil)            ; If list is empty, return nil
        ((> from to) nil)             ; If from index is greater than to, return nil
        (t 
            (let ((sub lst))                         ; Copy lst to new list 
                 (get-sub sub from to 1)             ; Call recursive function to get the sub list
            )                       
        )
    )
       
)

(print (sub-list2 '(1 4 10) 2 3))
(print (sub-list2 '(1 4 10) 2))
(print (sub-list2 '(1 7 12) 1 4))
(print (sub-list2 '(1 7 12) 0 1))
(print (sub-list2 '(1 6 12) 4 2))
(print (sub-list2 '(1 6 12)))