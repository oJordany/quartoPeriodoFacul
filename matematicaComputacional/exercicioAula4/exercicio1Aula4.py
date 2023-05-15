import numpy as np

def showTableWithValuesOfX(function, *XValues):
    for XValue in XValues[0]:
        print(XValue, ' → ',function(XValue))



showTableWithValuesOfX(lambda x: x**2 -4*x + 4, np.arange(0,4,0.5).tolist())

