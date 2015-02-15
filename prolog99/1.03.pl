element_at(H,[H|_],1).
element_at(X,[_|T],Count) :- NewCount is Count - 1, element_at(X,T,NewCount).

