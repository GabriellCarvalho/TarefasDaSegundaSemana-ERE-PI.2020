# -*- coding: utf-8 -*-

import cv2

#Função para mostrar uma imagem na tela
def show_image(image):
    cv2.imshow('',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Função para colar uma imagem em outra
def paste(Img, imagem2, x, y):
    Img[y:y + imagem2.shape[0], x:x + imagem2.shape[1]] = imagem2
    show_image(Img)

#Lendo as imagens
Img = cv2.imread('leao.jpg')
imagem_olho = cv2.imread('imagemCortada.jpg')

x = 112
y = 74

#Chamando a função paste()
Img = paste(Img,imagem_olho,x,y)


