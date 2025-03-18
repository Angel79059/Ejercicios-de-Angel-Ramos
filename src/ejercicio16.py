presentación = """
                  Este es el programa que puede calcular el 
                  factorial de un número.
                  
                  """

numero= """
             Ingresa el número. Debe ser un número entero: """

print(presentación)

numero = int(input('Ingresa un número entero: '))
factorial = 1

for i in range(1, numero + 1):
    factorial *= i

print(f'El factorial del {numero} es {factorial}')

