valoresDeXi = [0.5, 0.11]


def truncar(num, n):
    inteiro = int(num * (10**n))/(10**n)
    return float(inteiro)


def somatorio(valorDeXi, limiteInferior, limiteSuperior):
    resultado = 0
    for i in range(limiteInferior, limiteSuperior+1):
        resultado += valorDeXi
    return resultado


resultadosDoSomatorio = {
    valorDeXi: somatorio(valorDeXi, 1, 30000)
    for valorDeXi in valoresDeXi
}

for valorDeXi, resultadoDoSomatorio in resultadosDoSomatorio.items():
    print(f'Somatório para xi = {valorDeXi}: {resultadoDoSomatorio}')


# APRESENTANDO ERRO DE ARREDONDAMENTO
print(f'{" ERRO DE ARREDONDAMENTO ":#^60}')
print(f"{truncar(resultadoDoSomatorio, 11)}")

# APRESENTANDO ERRO DE OVERFLOW
print(f'{" ERRO DE OVERFLOW ":#^60}')
print(f"{round(resultadoDoSomatorio, 11)}")
