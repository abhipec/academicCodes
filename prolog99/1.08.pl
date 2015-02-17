find([H|_],Y) :- H == Y,!.
find([H|T],Y) :- \+ H == Y , find(T,Y).


compress(L,R) :- compress(L,[],R).

compress([],A,A).
compress([H|T],A,R) :-
    \+ find(A,H),
    append(A,[H],Anew),
    compress(T,Anew,R).
	
compress([H|T],A,R) :-
 	find(A,H),
    compress(T,A,R).

compressAlt([],[]).
compressAlt([X],[X]).
compressAlt([X,X|T],R) :-
    compressAlt([X|T],R).

compressAlt([X,Y|T],[X|R]) :-
    X \= Y,
    compressAlt([Y|T],R).
    
