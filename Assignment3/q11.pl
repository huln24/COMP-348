lucas(1, 2):-!.
lucas(2, 1):-!.
lucas(N, Lucas):- Np is N - 1,
    			Npp is N - 2,
    			lucas(Np, N1),
                lucas(Npp, N2),
                Lucas is N1 + N2.

first_n(0, []):-!.
first_n(N, Seq):-lucas(N, L1),
    			Prev is N - 1,
    			first_n(Prev, L2),
    			append(L2, [L1], Seq).


/*
Queries:

first_n(1, L).
L = [2]

first_n(2, L).
L = [2, 1]

first_n(5, L).
L = [2, 1, 3, 4, 7]
*/