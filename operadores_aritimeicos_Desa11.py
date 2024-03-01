largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = altura * largura 
tinta = 2
litrotinta = area // tinta

print(f'A area dessa parede mede: {area}, e a quantidade de tinta em litros é: {litrotinta}')
