inicio(q0).
final(q2).

p(q0,'a',q1).
p(q0,'e',q0).
p(q0,'i',q0).
p(q0,'o',q0).
p(q0,'u',q0).

p(q1,'e',q2).
p(q1,'a',q1).
p(q1,'i',q1).
p(q1,'o',q1).
p(q1,'u',q1).

p(q2,'i',q3).
p(q2,'a',q2).
p(q2,'e',q2).
p(q2,'o',q2).
p(q2,'u',q2).


p(q3,'o',q4).
p(q3,'a',q3).
p(q3,'e',q3).
p(q3,'i',q3).
p(q3,'u',q3).

p(q4,'u',q5).
p(q4,'a',q4).
p(q4,'e',q4).
p(q4,'i',q4).
p(q4,'o',q4).

p(q5,'a',q5).
p(q5,'e',q5).
p(q5,'i',q5).
p(q5,'o',q5).
p(q5,'u',q5).


teste(X) :- string_chars(X, Fita),
		 	inicio(No),
			reconhecedor(No, Fita), !.

reconhecedor(No,[]) :- final(No), !.
reconhecedor(De,[]) :- p(De, 'ε', Para),
					   reconhecedor(Para, []).
reconhecedor(De,Fita) :- p(De, 'ε', Para),
    					 reconhecedor(Para, Fita).
reconhecedor(De,Fita) :- p(De, X, Para),
                 		 X \== 'ε', 
						 caminha(X, Fita, Nova_Fita),
						 reconhecedor(Para, Nova_Fita).

caminha(H,[H | T],T).