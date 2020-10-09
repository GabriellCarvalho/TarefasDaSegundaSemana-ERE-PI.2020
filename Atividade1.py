# -*- coding: utf-8 -*-

import cv2

#Função para mostrar uma imagem na tela
def show_image(image):
    cv2.imshow('',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Função para recortar uma imagem 
def crop(imagem,posicao_x,posicao_y,largura,altura):
    new_image = imagem[posicao_y:posicao_y + altura, posicao_x:posicao_x + largura]
    return new_image

#Lendo uma imagem
Img = cv2.imread('leao.jpg')

posicao_x = 156
posicao_y = 106
largura = 55
altura = 55

#Chamando a função crop() 
img_cortada = crop(Img, posicao_x, posicao_y, largura, altura)

#Chamando a função show_image()
show_image(img_cortada)

#Salvando a imagem cortada
cv2.imwrite('imagemCortada.jpg',img_cortada)
