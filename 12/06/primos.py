import sys 

n = int(input('Quantidade de números primos: '))
if n <= 0:
    sys.exit('Encerrado!')

contPrimo = 0
numero = 2

while contPrimo < n:
    contDivisores = 0
   

    for i in range (1, numero + 1):
    
    if numero % i == 0: contDivisores += 1
    
    if contDivisores > 2: break

    if contDivisores == 2:
        print(numero)
        contPrimo += 1
        numero    += 1
