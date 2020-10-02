#!/usr/bin/env python3

#aqui vamos importar o sys para pegar os argumentos na linha de comando

import sys

#aqui vamos aceitar os 5 argumentos: a sequência de  DNA e as 4 coordenadas de posição

dna = sys.argv[1]

n1 = int(sys.argv[2])
n2 = int(sys.argv[3])
n3 = int(sys.argv[4])
n4 = int(sys.argv[5]) 

#agora vamos conferir se os dados passados estão nos formatos e tamanhos corretos e imprimir mensagens de confirmação ou erro

if isinstance(dna, str) == True and isinstance(n1, int) == True and isinstance(n2, int) == True and isinstance(n3, int) == True and isinstance(n4, int) == True:
	print("os objetos inseridos pelo usuário são do tipo correto")
	if (n1 < len(dna) and n2 < len(dna) and n3 < len(dna) and n4 < len(dna)):
		print("as coordenadas inseridas tem o tamanho adequado")
	else:
		print("n1 é maior que a sequência de dna") 
else:
	print("os objetos inseridos pelo usuário são do tipo errado") 

#aqui vamos extrair a sequência do CDS 1

CDS_1 = dna[n1 - 1:n2]

print("a sequência do CDS 1 é ", CDS_1)

#aqui vamos conferir se a sequência do CDS 1 começa com ATG

if CDS_1[0:3] == "ATG":
	print("a sequência de CDS 1 inicia com ATG")
else:
	print("a sequência de CDS 1 não inicia com ATG")

#aqui vamos extrair a sequência do CDS 2

CDS_2 = dna[n3 - 1:n4]

print("a sequência do CDS 2 é ", CDS_2) 

#aqui vamos conferir por meio de código se CDS 2 termina com TAG, TAA ou TGA

if CDS_2[len(CDS_2) - 3: len(CDS_2)] == "TAG" or CDS_2[len(CDS_2) - 3: len(CDS_2)] == "TAA" or CDS_2[len(CDS_2) - 3: len(CDS_2)] == "TGA":
	print("a sequência do CDS 2 termina com um dos códons de parada: TAG, TAA ou TGA")
else:
	print("a sequência do CDS 2 não termina com um dos códons de parada") 

#como os itens anteriores são verdadeiros, vamos concatenar o CDS_1 e o CDS_2

print("as sequências concatenadas de CDS 1 e CDS 2: ", CDS_1 + CDS_2) 
