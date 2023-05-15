def calcularTermoATermo(x, num):
    resultado = 1
    for i in range(num, 0, -1):
        resultado *= x/i
    return resultado

def calculaExponencialPelaSerieDeTaylor():    
    n = int(input("Insira o n: "))
    x = float(input("Insira o x: "))
    resultado = 0

    for k in range(0, n):
        resultado += calcularTermoATermo(x, k)

    print(resultado)

while (True):
    calculaExponencialPelaSerieDeTaylor()
    resposta = input("Cacular outra vez? [S/N] ").upper().strip()[0]
    if resposta == "N":
        break