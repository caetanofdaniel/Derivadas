#newton_raphson()

from derivadas import derivada_central

from derivadas import derivada_central

def metodo_newton(f, x0, h, epsilon, kmax):
    x = x0

    for k in range(kmax):
        fx = f(x)

        if abs(fx) < epsilon:
            return x, k, True

        dfx = derivada_central(f, x, h)

        if abs(dfx) < 1e-12:
            raise ValueError("Derivada muito próxima de zero")

        x = x - fx / dfx

    return x, kmax, abs(f(x)) < epsilon