;Cases:
; Empty list 
; Wrong starting index < debut > fin
; Wrong end index 
; end index = NIL => to value = list-length 


; Auxiliary recursive function to get the sub list

(defun get-sub (sublst from to i)
    (if (= i to) (cons (car sublst) nil)    ; If current index = to index, construct new list with head of sublist and nil as tail
        (cond ((< i from) (get-sub (cdr sublst) from to (+ i 1)))     ; Before reaching from index, ignore head of the list
              ((>= i from) (cons (car sublst) (get-sub (cdr sublst) from to (+ i 1)))) 
              ; After reaching from index, construct a list with head of list and recursion of the tail
        )
    )
) 

; Takes a list and returns sub-list from start index to end index
(defun sub-list (lst from &optional (to nil))
    (if (equal to nil) (defparameter to (list-length lst) ()))        ; If to index not given (i.e. = nil), use as default value list length
    (cond ((null lst) nil)                                            ; If list is empty, return nil
        ((or (< from 1) (> from to) (> from (list-length lst))) nil)  ; If from index out of bounds, return nil
        ((or (< to from) (< to 1) (> to (list-length lst))) nil)      ; If to index out of bounds, return nil
        (t 
            (let ((sub lst))                                          ; Copy lst to new list 
                 (get-sub sub from to 1)                              ; Call recursive function with copy list to get the sub list
            )                       
        )
    )
       
)

(print (sub-list '(1 4 10) 2 3))
(print (sub-list '(1 4 10 23 4) 2))
(print (sub-list '(1 7 12) 1 4))
(print (sub-list '(1 7 12) 0 1))
(print (sub-list '(1 6 12) 4 2))
(print (sub-list '(1 6 12)))