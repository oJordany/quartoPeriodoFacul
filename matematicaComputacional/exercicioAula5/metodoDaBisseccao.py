def bisseccao(f, a, b, e):
    i=0
    ai=a
    bi=b

    while abs(bi-ai) > e:
        pi = (ai+bi)/2
        print("a{}: {};  b{}: {};  p{}: {};".format(i,ai,i,bi,i,pi))
        if f(ai)*f(pi)<0:
            bi = pi
        else:
            ai = pi
        i+=1

    x = (ai+bi)/2
    return [f'{x}', f'{f(x)}', f'{i}']

print(bisseccao(lambda x: x**2 -7*x + 9, 1, 5, 0.0001))