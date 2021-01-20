from datetime import date,time,datetime, timedelta
import datetime as datetime2


# data_atual = date.today()

# print(data_atual)

# data_teste = datetime(1993,10,12)
# data_teste_oficial = data_teste.strftime('%d/%m/%y')
# print(data_teste_oficial)

# print(data_atual.strftime('%d/%m/%Y')) 

# horario = time(hour=12,minute=39,second=30)
# print(horario)

# print(data_atual.ctime())


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    

wendel = Pessoa('wendel')

def formulario(pessoa):
    dia = raw_input("Dia do nascimento: ")
    mes = raw_input("Mes do nascimento: ")
    ano = raw_input("ano do nascimento: ")
    # nasc = datetime(ano,mes,dia)
    nasc_date = nasc.strftime('%y/%m/%d')
    data_atual = date.today()
    data_atual2 = data_atual.strftime('%y/%m/%d')
    return data_atual2

teste = date(1993,10,12)
print(teste)
print(formulario(wendel)) 