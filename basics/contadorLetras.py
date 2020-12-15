def contador_letras(lista):
    resultado = []
    for x in lista:
        total = len(x)
        resultado.append(total)
    return resultado

if __name__ == '__main__':
    lista = ['wendel','lea','claudio','bianca']
    print(contador_letras(lista))
