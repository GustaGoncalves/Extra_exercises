def digite_numero(mensagem):

 while True:
  try:

   numero=float(input(mensagem))

  except ValueError:

   print('Digite apenas números!')

  except Exception as erro:

   print('Alguma bosta eu fiz lol')

   print(type(erro))

  else:

   return (numero)


# Programa Principal

distancia_passageiro=digite_numero('Quantos quilômetros terá a viagem? (Km): ')

if distancia_passageiro>200:

 custo_quilometro=0.45

elif distancia_passageiro<=200:

 custo_quilometro=0.50

print('-'*30)

print(f'Para uma viagem de {distancia_passageiro:.2f} o custo por quilômetro é de R${custo_quilometro:.2f}')
print(f'O custo total da viagem é de R${distancia_passageiro*custo_quilometro:.2f}')