#!/usr/bin/env python3

# aqui vamos importar o sys para permitir pegar os valores de a e b direto da linha de comando

import sys

#aqui vamos testar se o valor de a e b são inteiros, usando a função isinstance () e se eles estão entre 0 e 1000,  e imprimir uma mensagem de confirmação ou de erro

verify_a = isinstance(int(sys.argv[1]), int)

verify_b = isinstance(int(sys.argv[2]), int)

if (verify_a == True and verify_b == True):
	print("os valores de a e b são inteiros")
	if (0 < int(sys.argv[1]) < 1000) and (0 < int(sys.argv[2]) < 1000): 
		print("os valores de a e b são inteiros e estão entre 0 e 1000")
	else:
		print("os valores de a e/ou b são inteiros mas não estão entre 0 e 1000") 
else:
	print("os valores de a e/ou b não são inteiros")


# aqui vamos calcular o quadrado da hipotenusa, que é dado pela fórmula matemática: hip^2 = a^2 + b^2 

hip_ao_quadrado = int(sys.argv[1])**2 + int(sys.argv[2])**2 
print("o quadrado da hipotenusa para o triângulo retângulo com lados a = {} e b = {}, é {}".format(int(sys.argv[1]), int(sys.argv[2]), hip_ao_quadrado))

