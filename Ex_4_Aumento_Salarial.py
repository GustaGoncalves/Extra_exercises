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

aumento_salario_alto=0.10
aumento_salario_baixo=0.15

salario_funcionario=digite_numero('Digite o seu salario: R$')

print('-'*30)

if salario_funcionario<=1250:

 print(f'Para um salário de R${salario_funcionario:.2f} o aumento é de R${salario_funcionario*aumento_salario_baixo:.2f}')

elif salario_funcionario>1250:

 print(f'Para um salário de R${salario_funcionario:.2f} o aumento é de R${salario_funcionario*aumento_salario_alto:.2f}')