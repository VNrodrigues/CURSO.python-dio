from datetime import date, time, datetime, timedelta


# Como recuperar a data atual (DATE)
data_atual = date.today()
data_atual_str = (data_atual.strftime('%A %B %Y'))
print(data_atual_str)

# Como gerar um horário (TIME)
horario = time(hour=15, minute=18, second=30)
print(horario.strftime('%H:%M:%S'))

# Retornar data e hora atual (DATETIME)
data_atual = datetime.now()
print(data_atual)
print(data_atual.strftime('%H:%M:%S'))
print(data_atual.strftime('%c'))
print(data_atual.day)
print(data_atual.year)

tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
print(tupla[data_atual.weekday()])
data_criada = datetime(2018, 6, 20, 15, 30, 20)
print(data_criada)
print(data_criada.strftime('%c'))

data_string = '01/01/2022 12:20:22'
data_conver = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
print(data_conver)

nova_data = data_conver - timedelta(days=365)
print(nova_data)