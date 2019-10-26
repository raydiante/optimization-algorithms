from math import *
import math 
import random


nV = 0
nA = 0
maxA =0
matrizA= []
matrizB= []


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

def checaSeFolha(vert,arv): #verifica de o vertice "vert" eh folha na arvore "arv"
	flag=0

	for x in arv:
		if x[0] == vert or x[1] == vert:
			flag += 1
	if flag>1:
		return 0
	else:
		return 1


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




def vizinhanca(arv,card,nvz,tl):


	#print "\n ",tl 
	global matrizB
	global maxA
	flag=0
	flag1=0
	t=0
	l=0
	nvizi=nvz

	#armazena os nos folha
	ordem=[]
	k=[]
	m=[]

	while flag1==0:
		#print "\n\n\n\n\n " 
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

		#print arv2
		if arv2 not in tl:
			flag1=1
		t+=1
		if t==20:
			nvizi+=1
			t=0
			l+=1
		if t==5:
			return arv
	return arv2

def construtivo(matriz,card):
	s=prim(matriz, card)
	s=matrizArestas(s)
	s=kcardtree(matriz, card,s)

	return s

def tabu(matriz,card):
	s=[]
	tl=[]
	sl=[] 
	i=0
	p=50
	k=0
	melhor = 0


	s=construtivo(matriz,card)
	melhor=calculaFMA(s)
	tl.append(s)
	while(k<(p*100)):
		sl= vizinhanca(s,card,2,tl)
		if sl not in tl:
			tl.append(sl)
		if s==sl:
			s=construtivo(matriz,card)
			if calculaFMA(s)<melhor:
					melhor= calculaFMA(s)
		if calculaFMA(sl)<melhor:
				melhor= calculaFMA(sl)
		k+=1
		#print tl
	print melhor


def Main():
	card=5
	matriz = entrada()
	r=[]
	m=[]

	tabu(matriz,card)

	
Main()

