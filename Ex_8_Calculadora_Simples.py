from os import system

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

tamanho_linha=35
lista_numeros=[]
lista_operacoes=[
 'SOMA',
 'SUBTRAÇÃO',
 'MULTIPLICAÇÃO',
 'DIVISÃO'
]

while True:
 system('cls')
 repetir=0

 for i in range(0,2):
  lista_numeros.append(digite_numero(f'({i+1}/2) Digite um número: '))


 while True:
  system('cls')

  print(f'Números informados: ',end='')
  for numero in lista_numeros:
   print(numero,end=' ')

  print('\n') # Necessário para que o método .center funcione, pois ele não centraliza se houver '\n' dentro da string

  print('OPERAÇÕES'.center(tamanho_linha))
  print('-'*tamanho_linha)

  for i in range(0,len(lista_operacoes)):
   print(f'[{i+1}] {lista_operacoes[i]}')

  operacao_escolhida=digite_numero('Qual operação deseja realizar? ')


  match operacao_escolhida:

   case 1: # Soma

    print(f'A soma dos valores é de {sum(lista_numeros)}')
    break

   case 2: # Subtração

    print(f'A subtração dos valores é de {lista_numeros[0]-lista_numeros[1]}')
    break

   case 3: # Multiplicação

    print(f'A multiplicação dos valores é de {lista_numeros[0]*lista_numeros[1]}')
    break

   case 4: # Divisão

    print(f'A divisão dos valores é de {lista_numeros[0]/lista_numeros[1]:.2f}')
    break

   case _: # Opção inválida

    print('Selecione uma opção válida!')

 print('-'*tamanho_linha)

 while True:
  repetir=digite_numero('Calcular novamente?\n[1] Sim\n[2] Não\n')

  if repetir>0 and repetir<=2:
   break

  print('Digite uma opção válida!')


 if repetir==2: # Flag finalizar programa
  break

 lista_numeros.clear()