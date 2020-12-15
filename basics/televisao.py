class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 4

    
    def ligar(self):
        if self.ligada == False:
            self.ligada = True
    
    def desligar(self):
        if self.ligada:
            self.ligada = False

    def aumentarCanal(self):
        self.canal+=1
        return self.canal

    def diminuirCanal(self):
        if self.canal >1:
            self.canal-=1
        return self.canal

if __name__ == '__name__':

    televisao = Televisao()
    print('televisao esta ligada: {}'.format(televisao.ligada))
    televisao.ligar()
    print('televisao esta ligada: {}'.format(televisao.ligada))
    print('canal sintonizado: {}'.format(televisao.canal))
    televisao.aumentarCanal()
    televisao.aumentarCanal()
    print('canal sintonizado: {}'.format(televisao.canal))
    televisao.desligar()
    print('televisao esta ligada: {}'.format(televisao.ligada))




    