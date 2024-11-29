'''
   Fazer um programa que fique lendo números inteiros solicitados ao usuário.

   Quando o usuário digitar 0, o programa deve finalizar e imprimir a soma de 
   todos os números digitados bem como a média aritmética.

   O valor 0 não deve entrar na média.
'''
soma = 0
cont = 0
while True:
    x = int(input('Digite um valor:'))
    
    if x == 0: break
    
    else:
        cont = cont + 1
        soma += x    

print(f'A soma dos números digitados é de {soma}')
print(f'Média da soma dos números calculados: {soma/cont} ')
