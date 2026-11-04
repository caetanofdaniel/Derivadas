import pandas as pd

#testar_valores_h()
#gerar_valores_x()
#criar_dataframe_funcao()
#criar_dataframe_derivada()
#criar_dataframe_completo()


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

def criar_dataframe_funcao(f, valores_x):
    dados = []

    for x in valores_x:
        dados.append({
            "x": x,
            "f(x)": f(x)
        })

    return pd.DataFrame(dados)

def criar_dataframe_derivada(f, valores_x, h):
    dados = []

    for x in valores_x:
        dados.append({
            "x": x,
            "Progressiva": derivada_progressiva(f, x, h),
            "Regressiva": derivada_regressiva(f, x, h),
            "Central": derivada_central(f, x, h)
        })

    return pd.DataFrame(dados)

def criar_dataframe_completo(f, valores_x, h):
    tabela_funcao = criar_dataframe_funcao(f, valores_x)
    tabela_derivadas = criar_dataframe_derivada(f, valores_x, 0.1)

    tabela_completa = pd.merge(
        tabela_funcao,
        tabela_derivadas,
        on= "x"
    )

    return tabela_completa
