start(q0).
final(q0).
final(q3).
final(q4).
transition(q0, 1, q1).
transition(q0, 0, q5).
transition(q1, 1, q2).
transition(q1, 0, q3).
transition(q2, 1, q2).
transition(q2, 0, q2).
transition(q3, 1, q2).
transition(q3, 0, q3).
transition(q4, 1, q2).
transition(q4, 0, q3).
transition(q5, 1, q4).
transition(q5, 0, q0).

accept(Xs):-start(Q), path(Q, Xs).
path(Q, [X|Xs]):-transition(Q, X, QI), path(QI, Xs).
path(Q, []):-final(Q).

/*
Example queries & Expected results

 * accept([0]).		 --> q0 -> q5 = False
 * accept([1]).		 --> q0 -> q1 = False
 * accept([0, 1]).   --> q0 -> q5 -> q4 = True
 * accept([1, 0]).   --> q0 -> q1 -> q3 = True




 * accept([0,1,0,1,1,0]).
 * q0 -> q5 -> q5 -> q3 -> q2 -> q2 -> q2 = False
 *    0     1      0     1     1     0
 * */

