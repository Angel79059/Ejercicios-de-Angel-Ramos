bienvenida = """
                Bienvenido a este programa que muestra la serie de 
                fibunnaci en los primeros 20 numeros.
                """ 
print (bienvenida)

def fibunacci(n):
    if n < 2:
        return n
    else: 
        return fibunacci (n-1) + fibunacci (n-2)

for i in range(20):
    print(fibunacci(i))