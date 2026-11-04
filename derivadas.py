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

def derivada(f, x, h, epsilon, kmax, metodo="central"):

    metodos = {
        "progressiva":derivada_regressiva,
        "regressiva":derivada_regressiva,
        "central":derivada_central
    }

    if metodo not in metodos:
        raise ValueError("Método inválido")

    if h <= 0 or epsilon <= 0 or kmax <= 1:
        raise ValueError("Parâmetros inválidos")

    calcular = metodos[metodo]

    anterior = calcular(f, x, h)

    for k in range(1, kmax + 1):
        novo_h = h / 2

        if x + novo_h == x or x - novo_h == x:
            return anterior, k - 1, False

        h = novo_h
        atual = calcular(f, x, h)

        erro = abs(atual - anterior)

        if erro < epsilon:
            return atual, k , True

        anterior = atual

    return anterior, kmax, False


