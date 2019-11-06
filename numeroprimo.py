numero = int(input("Digite um numero: "))
divisores = 0
for divisor in range(1, numero):
    if numero % divisor == 0:
        divisores = divisores + 1
        if divisores > 1:
          break
if divisores > 1:
  print("O Numero não é primo")
else:
  print("O Numero é primo")
