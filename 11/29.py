'''
   Fazer um programa que fique solicitando ao usuário para digitar um número
   inteiro e informe se o número é par ou ímpar. 
   
   O programa só deve encerrar quando o usuário digitar o número 0.
'''

while True:
    print('Descubra se seu número é par ou ìmpar! (Digite 0 para encerrar a sessão.)')
    x = int(input('Digite um número inteiro: '))
    
    if x == 0: break
    
    if x%2 == 0:
        print(f'O número {x} é par!')
    else:
        print(f'O número {x} é impar!')


print('Fim da sessão!')
