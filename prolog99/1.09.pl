pack(X,Y) :- pack(X,Y,[]).

pack([X],[R],A) :- append(A,[X],R).
pack([X,X|T],R,A) :- append(A,[X],Anew),pack([X|T],R,Anew).
pack([X,Y|T],[Anew|R],A) :- X \= Y, append(A,[X],Anew), pack([Y|T],R,[]).

