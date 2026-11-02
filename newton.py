#newton_raphson()
def newton_com_derivada_numerica(f, aproximacao_inicial, h=10**-5, tol=10**-6, max_iter=1000):
    
    x = aproximacao_inicial
    for i in range(max_iter):
        fx = f(x)
        
        dfx = (f(x + h) - f(x - h)) / (2 * h)
        
        if abs(dfx) < 1e-12:
            raise ValueError("Derivada numérica muito próxima de zero. O método falhou.")
            
        x_novo = x - (fx / dfx)
        
        if abs(x_novo - x) < tol:
            print(f"Convergiu na iteração {i+1}")
            return x_novo
            
        x = x_novo
        
    print("Número máximo de iterações atingido.")
    return x

def f(x):
    return x**3 - 6*x**2 + 11*x - 6


raiz = newton_com_derivada_numerica(f, aproximacao_inicial=0.5)
print(f"Raiz encontrada: {raiz:.6f}")
