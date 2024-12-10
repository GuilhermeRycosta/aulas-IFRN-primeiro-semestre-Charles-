frase = input('Digite uma frase: ')
frase = frase.strip()

#contando as barras de espaço (' ') não funciona. Posso colocar duas barras ou mais entre as palavras
'''barra = frase.count(' ') + 1

print(f'Na frase "{frase}" existem {barra} palavras.')
'''
intPosicao    = 0
intQtPalavras = 0
while intPosicao < len(frase):
   # Verifica se o caractere atual é um espaço em branco
   if frase[intPosicao] == ' ' and frase[intPosicao - 1] != ' ':  
      intQtPalavras += 1
   intPosicao += 1 

# verifica se a última palavra da frase não foi contabilizada
if frase[-1] != ' ': intQtPalavras += 1

# Exibe a quantidade de palavras na frase digitada
print(f'Quantidade de palavras na frase: {intQtPalavras}')
