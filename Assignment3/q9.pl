sublist(List, Start, Len, Sub):-append(L1, L2, List), 
    length(L1,Start), 
    length(L2, Y),
    Len =< Y,
    append(Sub, _, L2), 
    length(Sub, Len).


/*
Example Queries & Expected Answers

?- sublist([1, 2, 3, 4], 1, 2, O)
O = [2, 3].
?- sublist([1, 2, 3, 4], 0, 0, O)
O = []
?- sublist([1, 2, 3, 4], 0, 10, O)
false
*/
