cadeia = ['E', 'X', 'P', 'P', 'X', 'E', 'X', 'E', 'P']

def geraCadeia(numRep):
	genoma = ''
	cont = 0
	cont2 = 0
	while numRep >= (len(genoma) + 1):
		genomaAux = verificaCadeia(genoma, cadeia[cont])

		if genomaAux == '':
			cont2 += 1
			if(cont2 == 1000):
				aux3 = len(genoma)
				genoma = genoma[2:aux3 - 1]
				cont2 = 0
			
			cont += 1
			if cont >= 9:
				cont = 0
		else:
			genoma = genomaAux
			cont += 1
			if cont >= 9:
				cont = 0
	print(genoma)
def verificaCadeia(genAtual, genNova):

	if len(genAtual) == 0:
		genNova = genNova + genAtual
		return genNova
	
	aux = genAtual[0: len(genNova)]

	if genNova == aux:
		return ''
	else:
		genNova = genNova + genAtual[0]
		aux = genAtual[1:]
		genNova = verificaCadeia(aux, genNova)
		return genNova


a = int(input(''))
geraCadeia(a)
	