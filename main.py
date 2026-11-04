#main()

from funcao import funcao
from derivadas import derivada_progressiva

def main():
    x0 = 3
    h = 0.1
    epsilon = 0.0001
    kmax = 100

    print(funcao(x0))

    resultado = derivada_progressiva(funcao, x0, h)
    print(f"Derivada progressiva: {resultado:.4f}")

if __name__ == "__main__":
    main()