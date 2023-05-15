def mpf(f, phi, x0, e1=0.000001, e2=0.000001, it_max=1000000):
  if (abs(x0) < e1):
    return x0

  x = phi(x0)
  k = 0
  while (abs(f(x)) > e1 and abs(x - x0) > e2 and k < it_max):
    print(f'x={x}, f(x)={f(x)}, k={k}')
    x0 = x
    x = phi(x)
    k+=1
  
  return (x, f(x), k)

res = mpf(lambda x: x**2 + x - 6, lambda x: 6/x - 1, 2.75)
print(res)  

print(mpf(lambda x: x**2 -7*x + 9, lambda x: -9/(x-7), 1))