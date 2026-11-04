#main()

from funcao import funcao
from derivadas import derivada
from analise import testar_valores_h

def main():
    x0 = 3
    valores_h = [0.1, 0.01, 0.001, 0.0001]

    epsilon = 0.0001
    kmax = 100

    resultados = testar_valores_h(funcao, x0, valores_h)

    for item in resultados:
        print(item)

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