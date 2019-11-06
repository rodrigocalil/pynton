from math import *
try:
	ladoa = int(input("Digite o primeiro valor: "));
	ladob = int(input("Digite o segundo valor: "));
	ladoc = int(input("Digite o terceiro valor: "));
except:
        print("\nDigite apenas inteiros!");
        input();
if (ladoa > (ladob + ladoc)):
        print("\nNão é um triangulo!");
elif (ladob > 0 and ladoc > 0):
        print("\nÉ um triangulo");

        s=(ladoa+ladob+ladoc)/2;
        area=sqrt(s*(s-ladoa)*(s-ladob)*(s*ladoc));

        print("A área do triângulo é: {:.2f}.".format(area));
