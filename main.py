#main()

from funcao import funcao
from derivadas import derivada_progressiva, derivada_regressiva, derivada_central, derivada

def main():
    x0 = 3
    valores_h = [0.1, 0.01, 0.001, 0.0001]

    epsilon = 0.0001
    kmax = 100

    for h in valores_h:
        progressiva = derivada_progressiva(funcao, x0, h)
        regressiva = derivada_regressiva(funcao, x0, h)
        central = derivada_central(funcao, x0, h)

        print("\nh = ", h)
        print(f"Progressiva: {progressiva:.4f}")
        print(f"Regressiva: {regressiva:.4f}")
        print(f"Central: {central:.4f}")

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