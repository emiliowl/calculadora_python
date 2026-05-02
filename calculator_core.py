def soma(x, y):
    return x + y

def subtracao(p1, p2):
    return p1 - p2

def multiplicacao(v1, v2):
    return v1 * v2

def divisao(p1, p2):
    return p1 / p2

def exponenciacao(p1, p2):
    return p1 ** p2

def radiciacao(p1, p2):
    return p1 ** (1/p2)

def fatorial(i):
    r = i
    j = i
    while (j > 1):
        j = j - 1
        r = r * j
        
    return r 