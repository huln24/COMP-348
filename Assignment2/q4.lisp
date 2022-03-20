; Function to check if element is already in the list
(defun is-duplicate (lst elt)
    (defparameter copy lst)
    (let ((n 1))
        (loop
            (when (>= n (list-length lst)) (return nil))
            (if (equal (car copy) elt) (return t) ())
            (setf copy (cdr copy)) 
            (incf n)
        )       
    )
)

; Function to flatten the list
(defun flatten (lst)
    (if (null lst)        ; If list is empty return nil
        nil
        (if (atom (car lst))        ; If head of lst is an atom
            (cons (car lst) (flatten (cdr lst)))        ; Construct a list with head of list and recur on tail of the list
            (append (flatten (car lst)) (flatten (cdr lst))))))  ; If head lst is not an atom (i.e. a list), append flattened head of lst with flattened tail


(defun flatten-nums-nodup (lst)
    (defparameter copy (flatten lst))       ; Flattened copy of the list
    (defparameter lst1 '())                 ; New list to be returned, and to be compared for duplication
    (defparameter elt (car copy))           ; Current element to check for duplication and if it is a number
    (defparameter tail (cdr copy))          ; Tail of the copy list
    (loop
        (when (null elt) (return lst1))     ; End loop when reach end of copy list and return newly formed list
        (if (numberp elt)                   ; If current element is number
            (if (is-duplicate lst1 elt) ()  ; Check for duplication
                (setf lst1 (append lst1 (list elt)))    ; If not a duplicate append to the new list and update the new list
            )
        ()
        )
        (setf elt (car tail))               ; Set current element as next element
        (setf tail (cdr tail))              ; Set current tail as next tail
    ) 
) 

(print (flatten-nums-nodup '(1 2 (3 1) (a 2.5) (2 4.5) ((1 2) 7.8) (10))))