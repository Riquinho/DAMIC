import numpy as np

a = np.arange(0,30)

print a


b = np.resize(a, (4,6))

print b
per= int(raw_input("Digite o primeiro corte do eixo x"))
per2= int(raw_input("Digite o primeiro corte do eixo x")) +1
per3= int(raw_input("Digite o primeiro corte do eixo y"))
per4= int(raw_input("Digite o primeiro corte do eixo y")) +1

print(b[per:per2,per3:per4])
