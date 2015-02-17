%checked solution for hint
flat(X,[X]) :- \+ is_list(X).
flat([],[]). %empty list corner case
flat([H|T],L):- 
    flat(H,Hlist),
    flat(T,Tlist),
    append(Hlist,Tlist,L).

