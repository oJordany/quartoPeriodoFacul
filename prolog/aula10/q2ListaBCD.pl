:- dynamic memorize/1.

addFato(Nome, Aridade) :- dynamic Nome/Aridade.

memorize(Fato) :- \+ clause(Fato, _),               % Verifica se um fato existe arg1: Termo, arg2: Corpo (caso seja uma regra)
                  functor(Fato, Nome, Aridade),     % Pega o nome e a aridade de um termo passado no arg1
                  addFato(Nome, Aridade),
                  asserta(Fato).