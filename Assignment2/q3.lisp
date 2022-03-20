; Auxiliary recursive function to get the sub list

(defun get-sub (sublst from to i)
    (if (= i to) (cons (car sublst) nil)
        (cond ((< i from) (get-sub (cdr sublst) from to (+ i 1)))     ; Before reaching from index, ignore head of the list
              ((>= i from) (cons (car sublst) (get-sub (cdr sublst) from to (+ i 1)))) 
              ; After reaching from index, construct a list with head of list and recursion of the tail
        )
    )
) 

; Auxiliary recursive function to get reversed list
(defun reverse-list (lst)
    (cond ((null lst) '())
        (t (append (reverse-list (cdr lst)) (list (car lst))))
    )
)


(defun sub-list3 (lst from &optional (to nil))
    (defparameter length (list-length lst))
    (if (or (equal to nil) (> to length)) (defparameter to length) ()) ; If to index not given or out of bound, use list length as default value 
    (if (< from 1) (defparameter from 1) ())                 ; If from index is out ouf bound, use 1 as default value
    (if (> from length) (defparameter from length) ())
    (if (< to 1) (defparameter to 1) ())
    (cond ((null lst) nil)                        ; If list is empty, return nil                         
        ; If from index is greater than to, return elements from the list in reverse order starting from to and ending with from 
        ((> from to) 
             (get-sub (reverse-list lst) (+ (- length from) 1) (+ (- length to) 1) 1)) ;from = list-length - from + 1  ,to = list-length - to + 1 
                                                      
        (t 
            (let ((sub lst))                      ; Copy lst to new list 
                 (get-sub sub from to 1)          ; Call recursive function to get the sub list
            )                       
        )
    )      
)


(print (sub-list3 '(1 4 10) 3 2))
(print (sub-list3 '(1 4 10) 3))
(print (sub-list3 '(1 7 12) 4 0))
(print (sub-list3 '(1 6 12)))