:- dynamic pos/2.
:- dynamic mochila/1.


pos(robo, garagem).
pos(tv, sala).
pos(bola, quarto).
pos(carteira, quarto).
pos(chave, garagem).

contain(H, [H | _]) :- !.
contain(Item, [_ | T]) :- contain(Item, T).
                          

ande(Destino) :- retract(pos(robo, X)),
                 asserta(pos(robo, Destino)),
                 format('Robo ande de ~w para ~w', [X, Destino]).

onde :- pos(robo, Local),
        format('O robo esta no(a) ~w', [Local]).

objetos :-  pos(robo, Local),
            findall(Objeto, pos(Objeto, Local), [_|Bag]),
            write(Bag).

pegue(ObjetoADD) :- pos(robo, Local),
                    findall(Objeto, pos(Objeto, Local), [_|Bag]),
                    contain(ObjetoADD, Bag),
                    asserta(mochila(ObjetoADD)),
                    retract(pos(ObjetoADD, Local)),
                    format('O robô colocou ~w na mochila', [ObjetoADD]).

mochila :- findall(Objeto, mochila(Objeto), Bag),
           write(Bag).

solte(Objeto) :- findall(Objeto, mochila(Objeto), Bag),
                 contain(Objeto, Bag),
                 pos(robo, Local),
                 retract(mochila(Objeto)),
                 assertz(pos(Objeto, Local)),
                 format('O robo soltou ~w na(o) ~w', [Objeto, Local]).