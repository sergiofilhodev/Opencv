import numpy as np # Para trabalhar com objetos, já que a imagem já é uma matriz.
import cv2 # Importando a biblioteca.
from matplotlib import pyplot as print # print é o apilido que eu dei pro matplotlib, tem que instalar o matplotlib: 'i matplotlib'.
img = cv2.imread('img/eu.jpg') # Carrega a imagem armazenando-a em uma variavel.
# cv2.imshow('imagem', cv2.imread('eu.jpg', cv2.IMREAD_ANYCOLOR)) # Exibir a imagem, Primeiro recebe o nome da janela e depois a variavel que está carregada a imagem.
# cv2.waitKey() # Essa função deixa o a janela aberta até que ela sejá fechada.
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # esse color significa a decodificação dele de cores, por exemplo: o a padrão do matplotlib é a bgr só que usando isso ele converte para rgb.
print.imshow(img)
print.show()