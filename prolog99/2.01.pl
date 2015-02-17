%not best algorithm
prime(_,1). 
prime(N,V) :- \+ is(0,mod(N,V)), Vnew is V - 1, prime(N,Vnew).
is_prime(1).
is_prime(N) :- integer(N), V is N - 1, prime(N,V).
