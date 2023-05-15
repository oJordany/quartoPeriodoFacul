class InterpoladorLagrange():

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def interpolarEm(self, xp):
        __grau = len(self.x) - 1
        __yp = 0 #VALOR INCIAL DO PONTO EM y
        for k in range(0, __grau+1):
            L = 1
            for j in range(0, __grau+1):
                if k != j :
                    L = L*(xp - self.x[j])/(self.x[k] - self.x[j])
            
            __yp = __yp + L*self.y[k]
    
        return __yp
    

    def plotarGraficoNoPonto(self, xp, yp):
        import matplotlib.pyplot as plt
        import numpy as np
        
        XsDaCurva = np.arange(self.x[0], self.x[-1], 0.1)
        YsDaCurva = [self.interpolarEm(x) for x in XsDaCurva]
        plt.plot(XsDaCurva, YsDaCurva, 'b-') 
        plt.plot(self.x, self.y, 'ro')
        plt.plot(xp, yp, 'g*') 
        plt.show()

# x = [-1, 0 ,2]
# y = [4, 1, -1]
# xp = 0.5

# IL = InterpoladorLagrange(x, y)
# yp = IL.interpolarEm(xp)
# IL.plotarGraficoNoPonto(xp, yp)