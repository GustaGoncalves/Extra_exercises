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


idade_carro=digite_numero('Digite a idade do seu carro (anos): ')

if idade_carro<=3:

 print('Seu carro é bem novo!')

elif idade_carro>3:

 print('Tu tem um Civic ou um Palio')
