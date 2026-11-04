import matplotlib.pyplot as plt
from derivadas import derivada_central, derivada_progressiva, derivada_regressiva

#grafico_funcao()
#grafico_derivada()
#grafico_convergencia()
#grafico_newton()
#marcar_maximos_minimos()

def grafico_funcao(f, valores_x):
    valores_y = []

    for x in valores_x:
        valores_y.append(f(x))

    plt.figure(figsize=(8, 5))

    plt.plot(valores_x, valores_y, label="f(x)", color="blue")

    plt.title("Gráfico da Função")
    plt.xlabel("x")
    plt.ylabel("f(x)")

    plt.grid(True)
    plt.legend()

    plt.show()


def grafico_derivada(f, valores_x, h):
    progressiva = []
    regressiva = []
    central = []

    for x in valores_x:
        progressiva.append(derivada_progressiva(f, x, h))
        regressiva.append(derivada_regressiva(f, x, h))
        central.append(derivada_central(f, x, h))

    plt.figure(figsize=(8, 5))

    plt.plot(valores_x, progressiva, label="Progressiva")
    plt.plot(valores_x, regressiva, label="Regressiva")
    plt.plot(valores_x, central, label="Central")

    plt.title("Comparação das Derivadas Numéricas")
    plt.xlabel("x")
    plt.ylabel("f'(x)")

    plt.grid(True)
    plt.legend()

    plt.show()


def grafico_convergencia(resultados):
    valores_h = []
    progressiva = []
    regressiva = []
    central = []

    for item in resultados:
        valores_h.append(item["h"])
        progressiva.append(item["progressiva"])
        regressiva.append(item["regressiva"])
        central.append(item["central"])

    plt.figure(figsize=(8, 5))

    plt.plot(valores_h, progressiva, marker="o", label="Progressiva")
    plt.plot(valores_h, regressiva, marker="s", label="Regressiva")
    plt.plot(valores_h, central, marker="^", label="Central")

    plt.xscale("log")
    plt.gca().invert_xaxis()

    plt.title("Convergência das Derivadas Numéricas")
    plt.xlabel("Passo h")
    plt.ylabel("Aproximação da derivada")

    plt.grid(True)
    plt.legend()

    plt.show()


def grafico_newton(f, valores_x, historico):
    valores_y = []

    for x in valores_x:
        valores_y.append(f(x))

    plt.figure(figsize=(8, 5))

    plt.plot(valores_x, valores_y, label="f(x)")
    plt.axhline(0, linestyle="--", color="gray")

    for k in range(len(historico) - 1):
        x_atual = historico[k]
        x_proximo = historico[k + 1]

        plt.scatter(x_atual, f(x_atual))

        plt.plot(
            [x_atual, x_proximo],
            [f(x_atual), 0],
            linestyle="--"
        )

        plt.plot(
            [x_proximo, x_proximo],
            [0, f(x_proximo)],
            linestyle=":"
        )

    plt.scatter(
        historico[-1],
        f(historico[-1]),
        label="Raiz aproximada"
    )

    plt.title("Método de Newton-Raphson")
    plt.xlabel("x")
    plt.ylabel("f(x)")

    plt.grid(True)
    plt.legend()

    plt.show()


def marcar_maximos_minimos(f, valores_x, classificados):
    valores_y = []

    for x in valores_x:
        valores_y.append(f(x))

    plt.figure(figsize=(8, 5))

    plt.plot(valores_x, valores_y, label="f(x)")

    for ponto in classificados:
        x = ponto["x"]
        y = ponto["f(x)"]
        classificacao = ponto["classificacao"]

        if classificacao == "Mínimo local":
            plt.scatter(x, y, color="green", s=100)
            plt.annotate("Mínimo local", (x, y))

        elif classificacao == "Máximo local":
            plt.scatter(x, y, color="red", s=100)
            plt.annotate("Máximo local", (x, y))

    plt.title("Máximos e Mínimos Locais")
    plt.xlabel("x")
    plt.ylabel("f(x)")

    plt.grid(True)
    plt.legend()

    plt.show()
