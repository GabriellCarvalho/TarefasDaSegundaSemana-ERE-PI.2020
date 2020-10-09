# -*- coding: utf-8 -*-

import cv2

imagem_colorida = cv2.imread('leao.jpg')

#Separando os canais de cores
canal_azul, canal_verde, canal_vermelho = cv2.split(imagem_colorida)

#Mostrando os canais de cores
#cv2.imshow('Canal Azul', canal_azul)
#cv2.imshow('Canal Verde', canal_verde)
#cv2.imshow('Canal Vermelho', canal_vermelho)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#Calculando a media 
#Azul
mediaAzul = 0
for y in range (0, canal_azul.shape[1]):
    for x in range(0, canal_azul.shape[0]):
        mediaAzul = mediaAzul + canal_azul[x][y]
mediaAzul = mediaAzul/(canal_azul.size)
#Vermelho
mediaVermelho = 0
for y in range (0, canal_vermelho.shape[1]):
    for x in range(0, canal_vermelho.shape[0]):
        mediaVermelho = mediaVermelho + canal_vermelho[x][y]
mediaVermelho = mediaVermelho/(canal_vermelho.size)
#Verde
mediaVerde = 0
for y in range (0, canal_verde.shape[1]):
    for x in range(0, canal_verde.shape[0]):
        mediaVerde = mediaVerde + canal_verde[x][y]
mediaVerde = mediaVerde/(canal_verde.size)

if mediaAzul > mediaVerde and mediaAzul > mediaVermelho:
    print('Imagem mais Azul')
elif mediaVerde > mediaAzul and mediaVerde > mediaVermelho:
    print('Imagem mais Verde')
else:
    print('Imagem mais Vermelha')