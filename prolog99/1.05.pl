ar([],A,A).
ar([H|T],A,R) :- ar(T,[H|A],R).
rev(L,R) :- ar(L,[],R).
