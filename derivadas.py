#derivada_progressiva()
#derivada_regressiva()
#derivada_central()
#derivada()


def derivada_progressiva(f, x, h):
    return (f(x + h) - f(x)) / h
