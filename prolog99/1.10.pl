pack(X,Y) :- pack(X,Y,[]).
pack([],[]).
pack([X],[R],A) :- append(A,[X],R).
pack([X,X|T],R,A) :- append(A,[X],Anew),pack([X|T],R,Anew).
pack([X,Y|T],[Anew|R],A) :- X \= Y, append(A,[X],Anew), pack([Y|T],R,[]).

encode(X,Y) :- pack(X,Ynew), combine(Ynew,Y). %first implement 1.09 then combine its output

combine([H|T],[A|Y]) :- compute(H,A), combine(T,Y). 
combine([],[]).

compute([H|T],A) :- length([H|T],C), A = [C,H].

