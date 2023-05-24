:- dynamic liga/0.
:- dynamic desliga/0.
:- dynamic lampada/1.


lampada(apagada).

liga :- retract(lampada(_)),
        asserta(lampada(acesa)).

desliga :- retract(lampada(_)),
           asserta(lampada(apagada)).