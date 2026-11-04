#main()

from funcao import funcao
from derivadas import derivada
from dados import testar_valores_h, gerar_valores_x, criar_dataframe_funcao, criar_dataframe_derivada, criar_dataframe_completo
from newton import metodo_newton
from analise import analisar_convergencia, analisar_sinal, encontrar_pontos_criticos, classificar_pontos_criticos
from graficos import grafico_funcao, grafico_derivada, grafico_convergencia, grafico_newton, marcar_maximos_minimos

def main():
    x0 = 3
    valores_h = [0.1, 0.01, 0.001, 0.0001]

    epsilon = 0.0001
    kmax = 100

    resultados = testar_valores_h(funcao, x0, valores_h)

    for item in resultados:
        print(item)

    valores_x = gerar_valores_x(0, 5, 1)
    tabela = criar_dataframe_funcao(funcao, valores_x)
    print(tabela)
    grafico_funcao(funcao, valores_x)
    grafico_derivada(funcao, valores_x, 0.1)
    grafico_convergencia(resultados)


    tabela_derivadas = criar_dataframe_derivada(funcao, valores_x, 0.1)
    print("\nTabela das derivadas: ")
    print(tabela_derivadas)

    tabela_completa = criar_dataframe_completo(funcao, valores_x, 0.1)
    print("\nTabela completa: ")
    print(tabela_completa.to_string(
        index = False,
        float_format = lambda valor : f"{valor:.4f}"
    ))

    h_inicial = 0.1

    resultado, iteracoes, convergiu = derivada(
        funcao,
        x0,
        h_inicial,
        epsilon,
        kmax,
        "progressiva"
    )
    print()
    print(f"Resultado: {resultado:.6f}")
    print(f"Iterações: {iteracoes}")
    print(f"Convergência: {convergiu}")

    historico_newton = []

    raiz, iteracoes, convergiu = metodo_newton(
        funcao, x0, 0.001, epsilon, kmax, historico_newton
    )
    print()
    print(f"Raiz: {raiz:.6f}")
    print(f"Iterações: {iteracoes}")
    print(f"Convergência: {convergiu}")

    valores_grafico = gerar_valores_x(0, 5, 0.1)
    grafico_newton(funcao, valores_grafico, historico_newton)


    print("\nAnálise de convergência: ")

    convergiu_h = analisar_convergencia(
        resultados,
        epsilon,
        "progressiva"
    )

    print(f"Estabilizou: {convergiu_h}")

    sinais = analisar_sinal(funcao, valores_x, 0.1, epsilon)

    print("\nAnálise dos sinais: ")

    for item in sinais:
        print(item)

    pontos = encontrar_pontos_criticos(funcao, valores_x, 0.1, epsilon)

    print("\nPontos críticos econtrados:")

    for ponto in pontos:
        print(ponto)

    classificados = classificar_pontos_criticos(funcao, pontos, 0.1, epsilon)

    print("\nClassificação dos pontos críticos")

    for item in classificados:
        print(item)

    valores_grafico = gerar_valores_x(-3, 3, 0.1)

    marcar_maximos_minimos(
        funcao,
        valores_grafico,
        classificados
    )

if __name__ == "__main__":
    main()