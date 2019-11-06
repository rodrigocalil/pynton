new_string = ""
frase = input('Digite a frase: ')
for palavra in frase.split(" "):
    new_string += palavra[::-1]+" "
print('A frase invertida é: {}'.format(new_string))
