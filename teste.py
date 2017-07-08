divisao = int(raw_input("Informe o numero de fatias: "))


if (divisao == 2):
    divisaoy = 1

elif (divisao == (4 or 6 or 8 or 10)):
    divisaoy = 2

elif (divisao == (12 or 15 or 18)):
    divisaoy = 3

elif (divisao == (20 or 24 or 28)):
    divisaoy = 4

elif (divisao == (25 or 30)):
    divisaoy = 5

elif divisao == (40 or 50):
    divisaoy = 10

else:
    print "Divisao nao disponivel"
    print "Escolha entre os numeros: 2, 4, 6, 8, 10, 12, 15, 18, 20, 24, 25, 28, 30, 40, 50"
    divisaoy = 0

print divisao
print type(int(divisao))

print divisaoy