import os
import random
import parser
import re
os.system('clear')

equa = ''
i = 0
rolagens = []
soma_rolagens = 0

print('   Rolagem de dados')
equa = input('=========================\n')

mais = re.findall('\+[0-9]+', equa)
menos = re.findall('\-[0-9]+', equa)
mult = re.findall('\*[0-9]+', equa)
divi = re.findall('\/[0-9]+', equa)
dice = re.findall('[0-9]+d[0-9]+', equa)

equa = ''
operacoes = mult + mais + menos + divi
for operacao in operacoes:
    equa = equa + operacoes[i]
    i = i + 1

dado = dice[0]
d = dado.find('d')
qtde_dice = int(dado[:d])
tam_dice = int(dado[d+1:])

i = 1
while i <= qtde_dice:
    rolagens.append(random.randint(1, tam_dice))
    soma_rolagens = soma_rolagens + rolagens[-1]
    i = i+1

print(rolagens)
equa_final = str(soma_rolagens) + equa
print(equa_final)
result = parser.expr(equa_final).compile()
print(eval(result))
