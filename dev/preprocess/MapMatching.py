#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import pow,sqrt

# Algoritmo de mapmathing utilizando distãncia euclidiana 
# parâmetro pontos (ordenado por longitude)
# parâmetro vertices (ordenado por longitude)
def mapMatching(pontos, vertices):
	qtdVertices = len(vertices)
	qtdPontos = len(pontos)
	if(qtdVertices == 0 or qtdPontos == 0): 
		return
	batchPoints = []
	for ponto in pontos:
		verticeInicial = vertices[0] 
		verticeFinal = vertices[qtdVertices-1]
		iterator = range(qtdVertices)
		distVerticeInicial = distance(ponto, verticeInicial)
		distVerticeFinal = distance(ponto, verticeFinal)
		minDist = distVerticeInicial
		ponto.setVerticeProximo(verticeInicial.id)
		if(distVerticeFinal < distVerticeInicial):
			iterator.reverse()
			minDist = distVerticeFinal
			ponto.setVerticeProximo(verticeFinal.id)
		iterator.pop(0) #remove primeiro elemento
		iterator.pop() #remove último elemento
		for verticeIndex in iterator:
			vertice = vertices[verticeIndex]
			dist = distance(ponto, vertice)
			if(dist < minDist):
				minDist = dist
				ponto.setVerticeProximo(vertice.id)	
			elif (abs(vertice.longitude - ponto.longitude) > minDist): #caso a lista esteja ordenada pela longitude
				break
		batchPoints.append((ponto.verticeProximo,ponto.latitude,ponto.longitude), )
		#print str(ponto.longitude) + " - " + str(ponto.latitude) + " - " + str(ponto.verticeProximo)
	return batchPoints

def distance(ponto, vertice):
	return sqrt (pow((vertice.latitude - ponto.latitude),2.0) + pow((vertice.longitude - ponto.longitude),2.0))