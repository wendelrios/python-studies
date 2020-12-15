numeros = [10,20,30,40,50,60,70,80,90,100]

print('o maior numero da lista: {}'.format(max(numeros)))


pessoas = ('wendel','bianca','lea','claudio')
numeros_tupla = tuple(numeros)
print(numeros_tupla)
lista_numeros = list(numeros_tupla)
print(lista_numeros)
lista_numeros.pop(2)
print(lista_numeros)
lista_numeros.remove(70)
print(lista_numeros)


teste = ('wendel',10, 4.5)
print(teste)