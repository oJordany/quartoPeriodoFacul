import pandas as pd


class InterpoladorNewton():
    def __init__(self, x, y, grau):
        self.x = x 
        self.y = y 
        self.n = len(x)
        self.grau = grau
    

    def construirTabelaDiferencaDividida(self):
        self.tdd = [[None for _ in range(self.n)] for _ in range(self.n)]
        
        for i in range(self.n):
            self.tdd[i][0] = self.y[i]

        for j in range(1, self.n):
            for i in range(self.n-j):
                self.tdd[i][j] = (self.tdd[i+1][j-1] - self.tdd[i][j-1])/(self.x[i+j] - self.x[i])
        
        return self.tdd
    

    def interpolarEm(self, xp):
        # COMBINANDO A TABELA DE DIFERENÇA DIVIDIDA COM OS (x - xi) → xterm
        __xterm = 1
        yp = self.tdd[0][0] # acumulador que inicia com d0 = f[x0] = primeira diferença dividida

        for ordem in range(1, grau+1):
            __xterm = __xterm*(xp - self.x[ordem-1])
            yp = yp + __xterm*self.tdd[0][ordem]

        return yp
        

    def plotarGraficoPonto(self, xp, yp):
        import matplotlib.pyplot as plt
        import numpy as np
        XsDaCurva = np.arange(self.x[0], self.x[-1], 0.01)
        YsDaCurva = [self.interpolarEm(_xp) for _xp in XsDaCurva]
        plt.plot(XsDaCurva, YsDaCurva, 'b-')
        plt.plot(self.x, self.y, 'ro')
        plt.plot(xp, yp, 'g*')
        plt.grid()
        plt.show()

x = [1, 1.01 , 1.02]
y = [1, 1.005, 1.01]
xp = 1.007
grau = 1
IN = InterpoladorNewton(x, y, grau)
tdd = IN.construirTabelaDiferencaDividida()
# PRINTANDO TABELA DE DIFERENÇA DIVIDIDA
tdd_df = pd.DataFrame(tdd)
print(tdd_df)
print('\n')
yp = IN.interpolarEm(xp)
IN.plotarGraficoPonto(xp, yp)
