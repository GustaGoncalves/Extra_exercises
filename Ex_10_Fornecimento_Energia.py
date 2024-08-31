from os import system

def digite_numero_inteiro(mensagem):

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

formatacao=40
instalacoes_tipos=[
 'RESIDENCIAL',
 'INDUSTRIAL',
 'COMERCIAL'
]

while True:
 system('cls')
 print('CUSTO DE ENERGIA'.center(formatacao))
 print('-'*formatacao)

 for i in range(0,len(instalacoes_tipos)):
  print(f'[{i+1}] {instalacoes_tipos[i]}')

 instalacao_usuario=digite_numero_inteiro('Qual o tipo de instalação: ')
 if instalacao_usuario>0 and instalacao_usuario<=len(instalacoes_tipos):
  break

energia_consumida=digite_numero_inteiro('Quanta energia é consumida?(kWh) ')

if instalacao_usuario==1: # Instalacão Residencial
 if energia_consumida<=500:
  preco_energia=energia_consumida*0.40

 elif energia_consumida>500:
  preco_energia=energia_consumida*0.65

elif instalacao_usuario==2: # Instalação Industrial
 if energia_consumida<=5000:
  preco_energia=energia_consumida*0.55

 elif energia_consumida>5000:
  preco_energia=energia_consumida*0.60

elif instalacao_usuario==3: # Instalação Comercial
 if energia_consumida<=1000:
  preco_energia=energia_consumida*0.55

 elif energia_consumida>1000:
  preco_energia=energia_consumida*0.60

system('cls')
print('CUSTO DE ENERGIA'.center(formatacao))
print('-'*formatacao)
print(f'Tipo de Instalação: {instalacoes_tipos[instalacao_usuario-1]}')
print(f'Preco da Energia: R${preco_energia:.2f}')