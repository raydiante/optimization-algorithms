from math import *
import math 
import random


nV = 0
nA = 0
maxA =0
matrizA= []
matrizB= []

def funcpop(): # decide a condicao de parada de acordo com o numero de arestas
	global nA
	if nA<100:
		return nA
	elif nA<1000:
		return 100
	else:
		return int(0.1*nA)

def condicaoElite(grafo, card):
	
	arv=prim(grafo, card)
	arv= matrizArestas(arv)
	s=kcardtree(grafo, card,arv)
	return calculaFMA(s)

def comparaArv(arv1,arv2): #verifica se arvore "arv1" eh igual a "arv2"
	flag=0
	k=[]

	if len(arv1) == len(arv2):
		for x in arv1:
			del k
			k=[]
			k.append(x[1])
			k.append(x[0])
			k.append(x[2])
			if x not in arv2 and k not in arv2:
				flag=1
				break
		if flag == 0:
			return 1 
	return 0

def checaSeFolha(vert,arv): #verifica de o vertice "vert" eh folha na arvore "arv"
	flag=0

	for x in arv:
		if x[0] == vert or x[1] == vert:
			flag += 1
	if flag>1:
		return 0
	else:
		return 1

def verificaArvMat(arv1,pop): #verifica se arvore "arv1" esta contida na matriz de arvorez "pop"
	flag=0
	flag2=0
	k=[]
	for arv2 in pop:
		if comparaArv(arv1,arv2) == 1:
			return 1
	return 0
def matrizArestas(arv): # transforma o vetor com os pais em um vetor de arestas
	p=[]
	for i in range(0,len(arv)):
		if(arv[i] != -1 and i!= arv[i]):
			m=[]
			m.append(i)
			m.append(arv[i])
			m.append(matrizB[i][arv[i]])
			p.append(m)
			del m
	return p

def calculaFMA(vv): #calcula peso das arestas da arvore "vv"
	suma=0
	for x in vv:
			suma=suma+ x[2]	
	return suma


def entrada(): # le as entradas


	global nV 
	global nA 
	global maxA 
	global matrizA
	global matrizB
	global maxA
	p= input()
	nV= input()
	nA = input()


	for i in range(0,nV):
		m=[]
		for j in range(nV):
			m.append(-1)
		matrizB.append(m)
		del m


	for i in range(0,nA):
		aresta = []
		entrada = raw_input() #ler os numeros
		separador = entrada.split('\t') #separador
		numeros = [float(numero) for numero in separador] # cria lista convertendo para float cada numero da entrada
		x, y, z = numeros
		x=int(x)
		y=int(y)
		aresta.append(x-1)
		aresta.append(y-1)
		aresta.append(z)
		matrizB[x-1][y-1]=z
		matrizB[y-1][x-1]=z
		matrizA.append(aresta)
		del aresta 
		if (maxA<z):
			maxA=z
	return matrizB



def gulosorand(): # acha arvore randomica
	resp = []
	k=0
	global nV 
	global nA 
	global matrizA

	matriz=matrizA
	n=0


	while(k==0):
		#coloca as arestas da sorte na respostas
		del resp
		resp = []
		n=0
		for x in matriz:
			ran=random.randint(0,1)
			if ran == 1:
				a=x[0]
				b=x[1]
				flag1=0
				flag2=0
				for y in resp: 
					if a == y[0] or a == y[1] :
						flag1=1
					if b == y[0] or b == y[1]:
						flag2=1
				#verifica se nao vai criar loop
				if flag1 == 0 or flag2==0:
					resp.append(x)
					n+=1
				if n < nV-1: # verifica se ja possui todas as arestas
					break

		#preenche o resto das arestas para criar uma arvore conexa
		for x in matriz:
			a=x[0]
			b=x[1]
			flag1=0
			flag2=0
			for y in resp:
				if a == y[0] or a == y[1] :
					flag1=1
				if b == y[0] or b == y[1]:
					flag2=1
			#verifica se nao vai criar loop
			if flag1 == 0 or flag2==0:
				resp.append(x)
		if len(resp)<(nV-1):
			k=0
		else:
			k=1
		break
	return resp


def prim(grafo, card):  # acha a arvore de valor minimo

	global nV 

	ori=random.randint(0,len(matrizB)-1)

	orig=ori
	arv=[]
	ordem=[]
	pai=[]
	visitados=[]
	for i in range(0,nV):
		arv.append(i)
		pai.append(-1)
	pai[orig]=orig
	visitados.append(orig)
	arv.remove(orig)
	#print grafo
	#print " \n\n"

	while (len(visitados) < nV):
		for x in visitados: 
			flag=1
			for i  in arv:
				if grafo[x][i] != -1  and flag==1	:
					menorp=grafo[x][i]
					orig=x
					dest=i
					flag=0
				elif grafo[x][i] != -1 :
					if menorp> grafo[x][i]:
						menorp= grafo[x][i]
						orig = x
						dest=i

		if pai[dest]==-1:
			pai[dest]=orig
			visitados.append(dest)
			arv.remove(dest)
		else:
			pai[orig]=dest

	return pai



def kcardtree(grafo, card,pai): #poda a arvore de acordo com card

	global nV 
	global matrizA 

	m=[]
	m.append(-1)
	z=-1
	card-=2

	ordem=[]
	maA=[]
	#print pai

	for x in pai:
		maA.append(x)

	#print maA
	
	#print " \n\n"

	#separa os nos folhas
	for i in range(0,len(pai)):
		count=0
		for x in maA:
			if x[0] == i or x[1] == i:
				count=count+1
		if count == 1:
			ordem.append(i)
	#print ordem


	#poda a arvore
	for i in range(0,(len(pai)-card-2)):
		maz = 0
		for k in ordem:
			for x in maA:
				if x[2] > maz and (k == x[0] or k == x[1]):
					maz= x[2]
					corte=k
					if corte == x[0]:
						z=x[1]
					else:
						z=x[0]
					m=x

		if m in maA:
			ordem.remove(corte)
			maA.remove(m)

		flag1=0
		for j in maA:
			if z == j[0] or z == j[1]:
				flag1=flag1+1
				x=j
		if flag1==1 :
			if corte == x[0]:
				ordem.append(z)
			else:
				ordem.append(z)
		#print maA
		#print  ordem
	return maA




def vizinhanca(arv,card,nvizi):


	global matrizB
	global maxA
	flag=0


	#armazena os nos folha
	ordem=[]
	k=[]
	m=[]

	for i in range(0,len(matrizB)):
		count=0
		for j in arv:
			if j[0]==i or j[1]==i:
				count=count+1
		if(count == 1):
			ordem.append(i)

	#pega os 4 vertices para serem trocados
	while flag==0:

		flag=0

		del k
		k=[]
		del m
		m=[]
		corteV=[]
		del corteV
		corteV = [] 
		corteA=[]
		del corteA
		corteA = [] 

		Vnovos = []
		w=0
		p=0
		q=0
		
		#pega os a folha a ser tirada e tira o pai dela tambem
		result = random.sample(range(0,len(ordem)),1)
		a=result[0]

		m.append(ordem[a])
		b=ordem[a]
		#print "ordem",ordem,a,b
		arv2=[]
		for x in arv:
			arv2.append(x)

		#print "-----"
		#print arv2

		for i in range(0,nvizi):
			flag=0
			corteV.append(b)
			for x in arv2:
				if x[0] == b  :
					b=x[1]
					flag=1
				elif x[1] == b:
					b=x[0]
					flag=1

				if flag == 1:
					arv2.remove(x)
					corteA.append(x)
					if checaSeFolha(b,arv2) == 0: # verifica se no seguinte eh no folha
						result=random.sample(range(0,len(ordem)),1) #pega outro no aleatorio para ser retirado
						while ordem[result[0]] in corteV :
							result=random.sample(range(0,len(ordem)),1)
						b=ordem[result[0]]
						#print result ,b

					break

		"""
		print "\narv2",arv2
		print "cortev",corteV
		print "corteA",corteA
		print "\n"
		"""

		#print corte,i,x
		#print len(corte)
		if len(corteA)!= 0:
			while w!=nvizi :
				maz =  maxA
				for x in arv2:
					if x[0] not in Vnovos:
						Vnovos.append(x[0])
					if x[1] not in Vnovos:
						Vnovos.append(x[1])
				for x in Vnovos:
					for j in range(0,len(matrizB)):
						#print len(matrizB), x,j
						if matrizB[x][j] != -1 and matrizB[x][j] < maz  and j not in Vnovos:
							if x in corteA[0]:
								del m
								m=[]
								m.append(x)
								m.append(j)
								m.append(matrizB[x][j])
								del k
								k=[]
								k.append(j)
								k.append(x)
								k.append(matrizB[j][x])
								if k not in arv and m not in arv:
									maz=matrizB[x][j]
									p=j
									q=x

							elif x not in corteA:
								maz=matrizB[x][j]
								p=j
								q=x
				del m
				m=[]
				m.append(p)
				m.append(q)
				m.append(maz)
				arv2.append(m)
				w=w+1
				#print arv2
		"""
		print len(arv2),len(arv)
		print "arv2",arv2
		print "\n"
		"""
		if (len(arv2) == len(arv)):
			flag=1
			break
		break
	return arv2


def population(matriz, card):
	populacao=[]
	k=0
	c=0
	cp=funcpop()
	while len(populacao) < cp:
		if c%2 == 0:
			arv=gulosorand()
			t=1
		else:
			arv=prim(matriz, card)
			arv=matrizArestas(arv)
			t=2
		s=kcardtree(matriz, card,arv)
		if verificaArvMat(s,populacao) == 0 and len(s)==card:
				arv=s
				k+=1
				populacao.append(arv)
		s=vizinhanca(s,card,3)
		if verificaArvMat(s,populacao) == 0 and len(s)==card:
				arv=s
				k+=1
				populacao.append(arv)
		c+=1
		if c>cp*200:
			break
	return populacao

def classifica(populacao,card): # classifica entre elite e plebe
	elite =[]
	plebe=[]
	aux=[]
	m=[]

	nElite=int(len(populacao)*0.15)
	if nElite==0:
		nElite=1


	for i in range(0,len(populacao)):
		del m
		m=[]
		m.append(calculaFMA(populacao[i]))
		aux.append(m)
	auxOrdenado=sorted(aux)


	if len(auxOrdenado)<=nElite:
		return populacao

	cp = auxOrdenado[nElite]

	for x in populacao:
		if calculaFMA(x)<=cp[0]:
			elite.append(x)
		if len(elite) == nElite:
			break
	return elite

def verificaGrafoConexo(arv,nos):
	aux=[]
	ares=[]
	nosVizitados=[]

	for x in arv:
		ares.append(x)

	nosVizitados.append(arv[0][0])
	nosVizitados.append(arv[0][1])

	for i in range(0,len(arv)):

		for x in ares:
			#print "-------",x
			if x[0] in nosVizitados:
				ares.remove(x)
				if x[1] not in nosVizitados:
					nosVizitados.append(x[1])
			elif x[1] in nosVizitados:
				ares.remove(x)
				if x[0] not in nosVizitados:
					nosVizitados.append(x[0])
			#print ares,"----",nosVizitados
			if len(ares)<=1 and (len(nos)-1)==len(nosVizitados):
				return 1

	#print len(ares),len(nos),len(nosVizitados),ares,nos,nosVizitados
	if len(ares)>1 or (len(nos)-1)!=len(nosVizitados):
		return 0
	else:
		return 1
def extraiminimo(d,q):

	#print "d-",d

	ds=sorted(d) #ordena lista

	#print "de-",ds,"\n",q

	for i in range(0,len(d)):
		if q[d.index(ds[i])] != -1:
			break

	#print i,d.index(ds[i]),ds[i]
	return d.index(ds[i]) #retorna a index do menor numero

def cpdj(q):
	
	for x in q:
		if x != -1:
			return 0
	return 1

def djisktra(matriz,ini,rec,nosd):
	#print "\n\n\n\n\n"
	pai=[]
	d=[]
	m=[]
	c=0
	q=[]
	resp=[]
	inf=float('inf')
	global matrizA

	for i in range(0,len(matriz)):
		d.append(inf)
		pai.append(-1)
		q.append(i)
	d[ini]=0

	while cpdj(q) == 0:
		#print "d -------",d
		u=q[extraiminimo(d,q)]
		#print  "atualiza", u
		q[extraiminimo(d,q)] =-1
		#print "djs"
		for i in range(0,len(matriz)):
			if matriz[u][i] != -1:
				if d[i]>d[u] + matriz[u][i]:
					d[i]=d[u] + matriz[u][i]
					pai[i]=u
				#print u,i
				#print pai
				#print d
				if i in nosd: # se conecta os dois ramos
					#print "here\n\n\n\n\n\n\n\n\n\n"
					#print i,pai[i]
					a=i
					b=pai[i]
					del resp
					resp=[]
					while c<100:
						del m
						m=[]
						m.append(a)
						m.append(b)
						m.append(matriz[a][b])
						resp.append(m)
						if b==ini:
							break
						#print b,pai[b]
						a=b
						b=pai[b]
						#print m,"\n\n\n\n\n\n\n"
					return resp

	return resp

def recombinacao(matriz,card,sol1,sol2):
	
	global matrizA
	c=0
	rec=[]
	nos=[]
	nosa=[]
	s=[]
	nosd=[]
	m=[]
	meio = int(len(matrizA)/2)

	for x in matrizA: # combina duas partes da solucao
		del m
		m=[]
		m.append(x[1])
		m.append(x[0])
		m.append(x[2])
		if c<meio: #a
			if x in sol1 or m in sol1 :
				rec.append(x)
				if x[0] not in nos:
					nos.append(x[0])
					nosa.append(x[0])
				if x[1] not in nos:
					nos.append(x[1])
					nosa.append(x[1])
		else: 	#d
			if x in sol2 or m in sol2:
				rec.append(x)
				if x[0] not in nos:
					nos.append(x[0])
					nosd.append(x[0])
				if x[1] not in nos:
					nos.append(x[1])
					nosd.append(x[1])
		c+=1
	


	if verificaGrafoConexo(rec,nos) == 0: #se grafo esta desconexo
		#print "\n\n\n\n\nconectar"
		#path relink
		ran=random.randint(0,nV-1) #escolhe um no
		while(ran not in nosa):
			ran=random.randint(0,nV-1)

		caminho=djisktra(matriz,ran,rec,nosd)

		for x in caminho:
			rec.append(x)

		s=kcardtree(matriz, card,rec)

	# se grafo esta conexo > faz a podagem se necessario
	if len(rec) > card: # podar
		s=kcardtree(matriz, card,rec)
		return s
	elif len(rec) < card: #adicionar mais arestas
		while len(rec)<card:
			ran=random.randint(0,len(matrizA)-1)
			x=matrizA[ran]
			del m
			m=[]
			m.append(x[1])
			m.append(x[0])
			m.append(x[2])
			if (m not in rec) and (x not in rec) and (x[1] in nos or x[0] in nos):
				rec.append(x)
		return rec
	else: #tamanho certo
		return rec



def genetico(matriz,card):

	cp=0

	#print"criando populacao"
	pop=population(matriz, card)
	tamPop=len(pop)

	while (cp<100):
		elite=classifica(pop,card)
		del pop
		pop=[]

		for x in elite:	
			pop.append(x)

		#print elite
		if len(elite)>1:
			for i in range (0, tamPop-len(elite)-1):
				#print len(elite)
				result = random.sample(range(0,len(elite)), 2)
				#print result
				a=result[0]
				b=result[1]
				pop.append(recombinacao(matriz,card,elite[a],elite[b]))
			tamPop=len(pop)
		cp+=1
	#print elite

	for x in elite:
		mini=float('inf')
		f=calculaFMA(x)
		if f<mini:
			mini=f

	return mini		
def Main():
	card=5
	matriz = entrada()
	r=[]
	m=[]

	print genetico(matriz,card)

	
Main()