x = int(input('Digite um valor: '))
y = 1
z = int(input('Digite o número máximo de multiplicadores: '))
print('Tabuada de {x}:')
while y <= z:
    print(f'{x} x {y} = {x*y}')
    y += 1
print(f'Fim da tabuada de {x}.')
