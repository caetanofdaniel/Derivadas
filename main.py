#main()

from funcao import funcao
from derivadas import derivada
from dados import testar_valores_h, gerar_valores_x, criar_dataframe_funcao, criar_dataframe_derivada, criar_dataframe_completo

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

if __name__ == "__main__":
    main()