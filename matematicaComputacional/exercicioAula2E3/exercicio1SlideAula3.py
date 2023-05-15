x1 = 0.1
x2 = 0.125

# Valores aproximados e Sa e Sb
Sa = 10000 - sum(x1 for _ in range(100000))
Sb = 10000 - sum(x2 for _ in range(80000))

# Valores reais de Sa e Sb
SaReal = 10000 - x1*100000
SbReal = 10000 - x2*80000

print(f"{' QUESTÃO a) ':#^60}")
print(f"Valor de S: {Sa}")
print(f"Erro absoluto: {abs(SaReal - Sa)}")
try:
    print(f"Erro relativo: {abs(SaReal - Sa)/abs(SaReal)}")
except Exception as err:
    print(f"Não há erro relativo: {err}")

print(f"{' QUESTÃO b) ':#^60}")
print(f"Valor de S: {Sb}")
print(f"Erro absoluto: {abs(0 - Sb)}")
try:
    print(f"Erro relativo: {abs(SbReal - Sb)/abs(SbReal)}")
except Exception as err:
    print(f"Não há erro relativo: {err}")
