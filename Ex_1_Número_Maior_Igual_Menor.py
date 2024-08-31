def digite_numero(mensagem):

 while True:
  try:

   numero=int(input(mensagem))

  except ValueError:

   print('Digite apenas números não decimais!')

  except Exception as erro:

   print('Alguma bosta eu fiz lol')

   print(type(erro))

  else:

   return (numero)
  

# Programa Principal

numero_main_1=digite_numero('Digite um número: ')
numero_main_2=digite_numero('Digite outro número: ')

if numero_main_1>numero_main_2:

 print(f'O número maior é {numero_main_1}')

elif numero_main_1<numero_main_2:

 print(f'O número maior é {numero_main_2}')

elif numero_main_1==numero_main_2:

 print(f'Os números são iguais')