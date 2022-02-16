import os
import random
import parser
os.system('clear')

i = 0
mais_proximo = []
rolagens = []
soma_rolagens = 0

print('   Rolagem de dados')
equa = input('=========================\n')

d = equa.find('d')
mais_proximo.append(int(equa.find('+')))
mais_proximo.append(int(equa.find('-')))
mais_proximo.append(int(equa.find('*')))
mais_proximo.append(int(equa.find('/')))
print(mais_proximo)
while i < len(mais_proximo):
    if mais_proximo[i] == -1:
        mais_proximo[i] = 999
    i = i+1

i = 1
print(mais_proximo)

mais = min(mais_proximo)
qtde_dice = int(equa[:d])
tam_dice = int(equa[d+1:mais])
cortado = equa[mais:]

while i <= qtde_dice:
    rolagens.append(random.randint(1, tam_dice))
    soma_rolagens = soma_rolagens + rolagens[-1]
    i = i+1

print(rolagens)
equa_final = str(soma_rolagens) + cortado
print(equa_final)
result = parser.expr(equa_final).compile()
print(eval(result))
