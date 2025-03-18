presentación = '''
                 Bienvenido a este programa que permite identificar si
                 un número es primo o no lo es.

                 Ingresa un número entero.
                '''

opcion_no_valida = '''
                     Ingresa una opción válida.
                     '''

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    opción = input(presentación)

    if opción.isdigit():
        numero = int(opción)

        if es_primo(numero):
            print(f"{numero} es un número primo.")
        else:
            print(f"{numero} no es un número primo.")
            
    else:
        print(opcion_no_valida)
        break

print('Gracias por usar este programa.')