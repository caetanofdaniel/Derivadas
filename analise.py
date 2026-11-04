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
