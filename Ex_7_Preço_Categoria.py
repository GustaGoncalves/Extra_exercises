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


def info_produto():

 nome_produto=input('Nome do Produto: ').strip()

 while True:

  numero_categoria=digite_numero('Categoria do Produto (De 1 até 5): ')

  if numero_categoria>=1 and numero_categoria<=5:

   return(
    nome_produto,
    numero_categoria
   )

  print('Digite uma categoria válida! (De 1 até 5)')


# Programa Principal

tabela_precos=[
 10.0,
 15.0,
 19.0,
 23.0,
 27.0
]

(
 nome_produto_main,
 categoria_produto
)=info_produto()
print('-'*30)

print(f'Nome: {nome_produto_main}')
print(f'Categoria: {categoria_produto}')
print(f'Preço: R${tabela_precos[categoria_produto-1]:.2f}')
