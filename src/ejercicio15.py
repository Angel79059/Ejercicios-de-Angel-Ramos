numeros = [1,2,3,4,5,6,7,8,9,10]

numeros_pares= [numero for numero in numeros if numero % 2 == 0]
numeros_impares=[numero for numero in numeros if numero % 2 > 0]

print('Los numeros pares son:')
print(numeros_pares)
print('Los numeros impares son:')
print(numeros_impares)

