#analisar_convergencia()
#analisar_sinal()
#encontrar_pontos_criticos()
#classicar_pontos_criticos()

from derivadas import derivada_central

def analisar_convergencia(resultados, epsilon, metodo="progressiva"):
    anterior = None
    convergiu = False

    for item in resultados:
        atual = item[metodo]

        if anterior is not None:
            diferenca = abs(atual - anterior)

            print(f"h = {item['h']}")
            print(f"Diferença = {diferenca:.8f}")

            convergiu = diferenca < epsilon

        anterior = atual

    return convergiu


def analisar_sinal(f, valores_x, h, epsilon):
    resultados = []

    for x in valores_x:
        derivada = derivada_central(f, x, h)

        if derivada > epsilon:
            sinal = "Crescente"

        elif derivada < -epsilon:
            sinal = "Decrescente"

        else:
            sinal = "Derivada próxima de zero"

        resultados.append({
            "x": x,
            "derivada": derivada,
            "sinal": sinal
        })

    return resultados

def encontrar_pontos_criticos(f, valores_x, h, epsilon):
    pontos = []

    for x in valores_x:
        derivada = derivada_central(f, x, h)

        if abs(derivada) < epsilon:
            pontos.append({
                "x": x,
                "f(x)": f(x),
                "derivada": derivada
            })

    return pontos


def classificar_pontos_criticos(f, pontos, h, epsilon):
    resultados = []

    for ponto in pontos:
        x = ponto["x"]

        esquerda = derivada_central(f, x - h, h)
        direita = derivada_central(f, x + h, h)

        if esquerda < -epsilon and direita > epsilon:
            classificacao = "Mínimo local"

        elif esquerda > epsilon and direita < -epsilon:
            classificacao = "Máximo local"

        elif (esquerda > epsilon and direita > epsilon) or (
            esquerda < -epsilon and direita < -epsilon
        ):
            classificacao = "Não é extremo local"

        else:
            classificacao = "Inconclusivo"

        resultados.append({
            "x": x,
            "f(x)": ponto["f(x)"],
            "classificacao": classificacao
        })

    return resultados
