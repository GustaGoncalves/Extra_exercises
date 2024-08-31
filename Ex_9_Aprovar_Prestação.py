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


def digite_numero_float(mensagem):

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

system('cls')
valor_formatação=40

print('BANCO AGI-OTA'.center(valor_formatação))
print('-'*valor_formatação)

valor_casa=digite_numero_float('Digite o valor da casa: R$')
salario=digite_numero_float('Digite o seu salário: R$')
anos_para_pagar=digite_numero_inteiro('Em quantos anos pretende pagar? ')
system('cls')

valor_prestacao_mes=valor_casa/(anos_para_pagar*12)

print('BANCO AGI-OTA'.center(valor_formatação))
print('-'*valor_formatação)
print(f'Valor da Casa: R${valor_casa:.2f}')
print(f'Valor da Prestação (mês): R${valor_prestacao_mes:.2f}')
print(f'Prazo Para Pagamento (anos): {anos_para_pagar}')
print(f'Salário Informado: R${salario:.2f}')
print('-'*valor_formatação)

if valor_prestacao_mes>(salario*(30/100)):

 print('\033[31mEMPRÉSTIMO NEGADO\033[m')
 print('O valor da prestação atual é muita alto e você não conseguirá pagar!')

elif valor_prestacao_mes<=(salario*(30/100)):

 print('\033[32mEMPRÉSTIMO APROVADO\033[m')
 print('Seu empréstimo foi aprovado!')
 print('Obrigado por escolher BANCO AGI-OTA')
