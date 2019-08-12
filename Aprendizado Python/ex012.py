print('Sistema de desconto')
produto = input('Digite o nome do produto: ')
preco = float(input('Digite o preço do produto: '))

desconto = (preco * 5) / 100
print('O produto {} teve {:.2}R$ de desconto na compra'.format(produto, desconto))
