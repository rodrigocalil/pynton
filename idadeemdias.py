qtddias = int(input('Digite a quantidade de dias:'))

anos = qtddias / 365

qtddias %= 365

meses = qtddias / 30

qtddias %= 30

dias = qtddias

print ("Resultado: " + str(dias) + " dias, " + str(meses) + " meses e " + str(anos) + " anos.")
