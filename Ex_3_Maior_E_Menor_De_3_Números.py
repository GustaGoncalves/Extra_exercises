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
lista_numeros=[]

for i in range(0,3):

 lista_numeros.append(digite_numero(f'({i+1}/3) Digite um número: '))

print('-'*30)

print('Os números digitados foram: ',end='')

for numero in lista_numeros:

 print(numero,end=' ')

print(f'\nO maior número digitado foi {max(lista_numeros)}')
print(f'O menor número digitado foi {min(lista_numeros)}')
