 
count_to_10(X,X):- write(X).

count_to_10(X,Y) :-
  write(X),nl,
  Z is X+1,
  Z =< Y,  
  count_to_10(Z,Y). 

