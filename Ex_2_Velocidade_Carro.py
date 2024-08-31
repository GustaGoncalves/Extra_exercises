def digite_numero(mensagem):
 
 while True:
  
  try:
   valor_velocidade=int(input(mensagem))

  except ValueError:

   print('Digite apenas números não decimais!')

  except Exception as erro:

   print('Alguma coisa eu fiz errado :P')
   print(erro.__class__)

  else:

   return valor_velocidade


# Programa Principal

valor_formatação=30

print('Calculadora de Multa'.center(valor_formatação))

print('-'*valor_formatação)

velocidade_carro=digite_numero('Digite a velocidade do carro Km')

if velocidade_carro<80:

 print()