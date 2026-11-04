#analisar_convergencia()
#analisar_sinal()
#encontrar_pontos_criticos()
#classicar_pontos_criticos()

from derivadas import derivada_progressiva, derivada_regressiva, derivada_central

def testar_valores_h(f, x0, valores_h):
    resultados = []

    for h in valores_h:
        progressiva = derivada_progressiva(f, x0, h)
        regressiva = derivada_regressiva(f, x0, h)
        central = derivada_central(f, x0, h)

        resultados.append({
            "h": h,
            "progressiva": progressiva,
            "regressiva": regressiva,
            "central": central,
        })
            

    return resultados

def gerar_valores_x(inicio, fim, passo):
    valores = []

    if passo <= 0:
        raise ValueError("O passo deve ser positivo")

    x = inicio

    while x <= fim:
        valores.append(round(x, 10))
        x += passo

    return valores
