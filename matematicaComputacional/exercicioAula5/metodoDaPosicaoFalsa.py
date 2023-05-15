def posicaoFalsa(f, a, b, e):
    i=0
    ai=a
    bi=b
    pi = (ai*f(bi)-bi*f(ai))/(f(bi) - f(ai))
    while abs(bi-ai) > e and abs(f(pi)) > e:
        pi = (ai*f(bi)-bi*f(ai))/(f(bi) - f(ai))
        print("a{}: {};  b{}: {};  p{}: {};".format(i,ai,i,bi,i,pi))
        if f(ai)*f(pi)<0:
            bi = pi
        else:
            ai = pi
        i+=1

    x = pi
    return [f'{x}', f'{f(x)}', f'{i}']

print(posicaoFalsa(lambda x: x**2 -4*x + 4, -1, 4, 0.00001))