def minimos_quadrados(x,y):
    from math import sqrt
    assert type(x) == list and type(y) == list, "Os parâmetros recebidos não são listas"
    assert len(x) == len(y), "As listas devem ter o mesmo tamanho"

    N = len(x)

    for i in range(N):
        bar_x = 0
        bar_y = 0
        bar_xy = 0
        bar_x2 = 0
        bar_y2 = 0
        bar_x += x[i]/N
        bar_y += y[i]/N
        bar_xy += (x[i]*y[i])/N
        bar_x2 += (x[i])**2/N
        bar_y2 += (y[i])**2/N
        
    Sxy = bar_xy - bar_x*bar_y
    Sxx = bar_x2 - bar_x**2
    Syy = bar_y2 - bar_y**2

    r = Sxy/sqrt(Sxx*Syy)

    a = Sxy/Sxx

    b = bar_y - a*bar_x

    print(a,b)