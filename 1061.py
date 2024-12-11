
#Posso transformar tudo em segundos subtrair o final do inicio e depois fazer resto da divisão com as horas minutos e segundos.
# tipo xxx segundos % com xxx horas transformadas em segundos, aqui vou ter o resto que depois uso em minutos
# e o resultado da divisão de xxx segundos // por horas em segundos será o resultado das horas, que converto de segundos para horas de novo
def time_event(dI,dF,init,fim):
  # sabendo o numero de dias de duração
  total_dias = dF - dI
  #transformando os dias em segundos
  dias_seg = total_dias * 86400

  #trasformando os valores de hora minuto e segundo em segundos somados
  inicio_segundos_total = (int(init[0]) * 3600) + (int(init[1]) * 60) + int(init[2])

  final_segundos_total = (int(fim[0]) * 3600) + (int(fim[1]) * 60) + int(fim[2])

  #pegando os segundos a serem calculados de fato
  # subtraindo o inicio e fim, assim tendo o valor do intervalo de tempo
  segundos_total = inicio_segundos_total - final_segundos_total

  #E aqui os segundos totais, pois subtraio os dias também, assim tenho o intervalo real de inicio ao fim
  soma_total = dias_seg - segundos_total

  #Aqui pego os valores já convertidos e 'mágica acontece'
  #onde o restante de um é o valor do próximo, dias, horas, minutos, segundos.
  dias = soma_total // 86400
  resto = soma_total % 86400
  horas = resto // 3600
  resto = resto % 3600
  minutos = resto // 60
  resto = resto % 60
  segundos = resto
  
  #imprimo tudo
  print(f'{dias} dia(s)')
  print(f'{horas} hora(s)')
  print(f'{minutos} minuto(s)')
  print(f'{segundos} segundo(s)')



if __name__ == '__main__':
  #leio e armazeno os valores
  diaI = int(input().split()[1])
  inicio = [c for c in input().split(' : ')]
  diaF = int(input().split()[1])
  final = [c for c in input().split(' : ')]

  #chamo a função
  time_event(diaI,diaF,inicio,final)

