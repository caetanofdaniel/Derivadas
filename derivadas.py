#derivada_progressiva()
#derivada_regressiva()
#derivada_central()
#derivada()


def derivada_progressiva(f, x, h):
    return (f(x + h) - f(x)) / h

def derivada_regressiva(f, x, h):
    return ((f(x) - f(x - h))) / h

def derivada_central(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)
