presentación = """
               Bienvenido a este programa que permite identificar si 
               dos palabras son anagramas o no."""

print(presentación)

def es_anagrama(palabra_1, palabra_2):
    return sorted(palabra_1) == sorted(palabra_2)

palabra_1= input('Introduce la primera palabra: ')
palabra_2= input('Introduce la segunda palabra: ')

if es_anagrama(palabra_1, palabra_2):
    print('Las palabras son anagramas.')
else:
    print('Las palabras no son anagramas.')




