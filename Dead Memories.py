print ('''

"Você acorda em uma sala destruida, maquinas quebradas, sons 
estranhos do lado de fora.
Você olha para suas mãos e estão secas e velhas sendo a direita 
totalmente esqueletica."

	''')

print("OQUE VOCÊ FAZ?")


print('''

[1] Procuro por uma arma
[2] Procuro alguém

	''')

escolha = input('escolha!')
if escolha == '1':
	print('você encontra um cabo de vasoura e está quebrada em sua ponta')
	
	print('VOCÊ GANHOU UMA LANÇA')
elif escolha == "2":
	print('Você encontra um cadâver que parece morto recentemente')
	
	print('''
		[1] encosto nele
		[2] analiso ele

		''')

escolha = input('ESCOLHA!')
if escolha == '1':
	print('''

		Você escosta no peito do cadâver e sua pele derrete e chamas 
		verdes saem de seus orificios como olhos, bocas conectando 
		todo seu corpo

		''')