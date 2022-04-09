get([], []):-!.    
get([_|T], T):-!. 

every-other([], []):-!.
every-other([H|T], Odds):-get(T, T1),
    					every-other(T1, L1),
    					append([H], L1, Odds).

/*efficient termination ex:  get([], []):-!. */

/*
Examples Queries:

?- every-other([], L)
L = [].
?- every-other([1], L)
L = [1].
?- every-other([1, 2], L)
L = [1].
?- every-other([1, 2, 3], L)
L = [1, 3].
?- every-other([1, 2, 3, 4], L)
L = [1, 3].
*/
  