prime_factors(N,L) :- 
    N > 0, prime_factors(N,2,[],L).

prime_factors(N,V,A,L) :-
    is(0,mod(N,V)),
    Nnew is N/V,
    append(A,[V],Anew),
    prime_factors(Nnew,V,Anew,L).

prime_factors(N,V,A,L) :-
    \+ is(0,mod(N,V)),
    V < N,
    Vnew is V + 1,
    prime_factors(N,Vnew,A,L).

prime_factors(1,_,L,L).

