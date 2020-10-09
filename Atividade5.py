# -*- coding: utf-8 -*-


import cv2 

#Função para mostrar uma imagem na tela
def show_image(image):
    cv2.imshow('',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#Carregado imagens 
messi = cv2.imread('messi.jpg')
cr7 = cv2.imread('CR7.jpg')

#redimensionando imagen
alturaMe, larguraMe, _ = messi.shape
cr7 = cv2.resize(cr7, (larguraMe,alturaMe))

#Juntando as imagens 
messinaldo = cv2.addWeighted(messi, 0.5, cr7, 0.5, 0)

#Mostrando o resultado final
show_image(messinaldo)

#salvando o resultado
cv2.imwrite('Messinaldo.jpg', messinaldo)