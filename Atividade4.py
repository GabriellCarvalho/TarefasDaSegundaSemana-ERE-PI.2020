# -*- coding: utf-8 -*-

import cv2


#Carregando imagem 
sonic = cv2.imread('sonic.jpg')


for y in range(0,sonic.shape[1]):
    for x in range(0,sonic.shape[0]):
        if sonic[x][y][0] > 50 and sonic[x][y][0] < 255 and sonic[x][y][1] < 100 and sonic[x][y][2] < 100:
            sonic[x][y][0] = 13
            sonic[x][y][1] = 240
            sonic[x][y][2] = 64
            
cv2.imshow('',sonic)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("sonicBR.jpg",sonic)