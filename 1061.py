
def time_event(dI,dF,init,fim):

  total_dias = dF - dI

  dias_seg = total_dias * 86400

  inicio_segundos_total = (int(init[0]) * 3600) + (int(init[1]) * 60) + int(init[2])

  final_segundos_total = (int(fim[0]) * 3600) + (int(fim[1]) * 60) + int(fim[2])

  segundos_total = inicio_segundos_total - final_segundos_total

  soma_total = dias_seg - segundos_total

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
  diaI = int(input().split()[1])
  inicio = [c for c in input().split(' : ')]
  diaF = int(input().split()[1])
  final = [c for c in input().split(' : ')]

  time_event(diaI,diaF,inicio,final)

