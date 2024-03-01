# nome = input('Qual o seu nome? ')
# print(f'Prazer em te conhecer {nome:^20}')

# se eu colocar :> o nome vai para o ultimo espaço, se eu colocar :^ o nome vai para o meio, e se eu colocar =^ vai ser adicionado

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2 
e = n1 ** n2 
print(f'A soma vale: {s}, o produto é {m}, e a divisão é {d:.3}')
print(f'A divisão inteira {di} e potência {e}')