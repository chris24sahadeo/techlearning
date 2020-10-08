; playing around with jess

; making a list of girls names
(bind ?girls (create$ "Aliyah" "Aarti" "Maria"))

; printing the list
(printout t ?girls crlf)

; printing the 2nd element in the list
; NB: why is 0 nil?
(bind ?position 2)
(printout t "The girl in the #" ?position " position is " (nth$ 2 ?girls) crlf)

; appending to list 
(bind ?girls (create$ ?girls "Nicander" "Shaundelle"))

; printing the new list
(printout t ?girls crlf)

; foreach
(printout t )
(foreach ?girl ?girls
    (printout t ?girl crlf))

; while
(bind ?num_girls 5)
(bind ?i 1)
(while (<= ?i ?num_girls)
    (printout t (nth$ ?i ?girls) crlf)
    (bind ?i (+ ?i 1)))