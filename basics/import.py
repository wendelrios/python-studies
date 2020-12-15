from televisao import Televisao
from contadorLetras import contador_letras

televisao = Televisao()

print(televisao.ligada)

if __name__ == '__main__':
    lista = ['fluminense', 'flamengo']
    print(contador_letras(lista))