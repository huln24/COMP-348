student(khulan, 40078465).
student(alice, 41067380).
is_taking(khulan, comp228).
is_taking(khulan, comp348).
is_taking(khulan, soen287).
is_taking(khulan, biol261).
is_taking(alice, comp249).
is_taking(alice, comp228).
is_taking(alice, comp233).
is_taking(alice, soen287).
course(comp228, 'system hardware').
course(comp348, 'principles of programming langugages').
course(soen287, 'web programming').
course(biol261, 'molecular and cellular genetics').
course(comp249, 'object oriented programming 2').
course(comp233, 'probability and statistics for computer science').


/*Give full course info = name + number taken by Name*/
course_full(Name, C ,F):-is_taking(Name, C), 
    X = C ,
    course(X, Y), 
    append([X], [Y], F).

/*Give size of a team*/
team_size(Size):-findall(X, student(X,_), L), length(L, Len), Size is Len.

/*Give iterable not unique courses*/
not_unique(Z):-course_full(X1, Y, Z), course_full(X2, Y, Z), X1 \= X2, Z = Z.

/*Give set of not unique courses*/
not_unique_set(Set):-findall(X, not_unique(X), L), list_to_set(L, Set).

/*Delete the specified element from the list*/
delete_element(_, [], []):-!.
delete_element(X, [X|T], R):-delete_element(X,T,R).
delete_element(X, [Y|T], [Y|T1]):-X \= Y, delete_element(X,T,T1).

/*Remove all elements in a list from another list*/
unique([], L, L):-!.
unique([H|T], L, UL):-delete_element(H, L, NL), unique(T, NL, UL).

/*Create list of unique classes taken by all the members*/
unique_courses(U):-not_unique_set(Set), 
    findall(X, course_full(_,_, X), Courses), 
    unique(Set, Courses, U).


/*Return list of courses taken by each member*/
%findall(X,course_full(khulan, _, X), L).

/*Return team size*/
%team_size(Size).

/*Return unique courses taken by the whole team*/
%unique_courses(Unique).

