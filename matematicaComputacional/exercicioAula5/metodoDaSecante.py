def metodoSecante(f, x0, x1, e1=0.0000001, e2=0.0000001, it_max=1000000):
    if abs(f(x0)) < e1:
        return x0
    
    if abs(f(x1)) < e1 and abs(x1 - x0) < e2:
        return x1
    
    x = x1 - (f(x1) / (f(x1)-f(x0))) * (x1-x0)
    k = 0

    while (abs(f(x)) > e1 and abs(x - x1) > e2 and k < it_max):
        print(f'x={x}, f(x)={x}, k={k}')
        x0 = x1
        x1 = x 
        x = x1 - ((f(x1) / (f(x1) - f(x0))) * (x1 - x0))
        k += 1

    return [f'{x}', f'{f(x)}', f'{k}']

print(metodoSecante(lambda x: x**2 -4*x + 4, -1, 4))