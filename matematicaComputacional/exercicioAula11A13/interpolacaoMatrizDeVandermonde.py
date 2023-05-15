
class InterpoladorVandermonde():

    def __init__(self, x, fx):
        self.x = x
        self.fx = fx

    def obterSistemaVandermonde(self):
        import numpy as np
        n = len(self.x)
        self.A = np.empty((n,n))
        self.b = np.empty((n))
        for i in range(0,n):
            self.A[i,0] = 1 # A primeira coluna da matriz de Vandermonde é sempre 1
            # PARA AS DEMAIS COLUNAS TEMOS:
            for j in range(1,n):
                self.A[i,j] = self.A[i, j-1] * self.x[i] # Só vai multiplicando x_0^1, x_0^2, ... , x_0^n (sendo que o x depende de qual linha vc tá)
            self.b[i] = self.fx[i]

        return self.A, self.b
    
    def resolver(self):
        import numpy as np
        x = np.linalg.solve(self.A, self.b)
        return x
    
# x = [-1, 0, 2]
# fx = [4, 1, -1]

# IV = InterpoladorVandermonde(x, fx)
# A, b = IV.obterSistemaVandermonde()
# xSolution = IV.resolver()
# print(A)
# print(b)
# print(xSolution)