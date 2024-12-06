import sys
n = int(input('Digite um valor: '))

if n<= 0: sys.exit('...')
strBinario = ''
while n > 0:
    resto      = n%2
    strBinario = str(resto) + strBinario
    n          = n//2

print(strBinario)