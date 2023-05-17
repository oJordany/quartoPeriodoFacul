import numpy as np
from itertools import permutations

vogais = np.array(['a', 'e', 'i', 'o', 'u'])
todasPermutacoes = np.array(list(permutations(vogais)))
for permutacao in todasPermutacoes:
    for i, vogal in enumerate(permutacao):
        with open('funcoesDeTransicao.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f"p(q{i}, \'{vogal}\', q{i+1}).\n")
    