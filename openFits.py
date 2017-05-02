import numpy as np 
import matplotlib
import matplotlib.pyplot as plt
import os
import glob
 
 
from astropy.utils.data import download_file
 
from astropy.io import fits
 
 
if not os.path.exists('imagens_fits'):
    os.makedirs('imagens_fits') #Cria a pasta
 
print('Por favor mova os arquivos fits para a pasta image fits')
resposta = raw_input('as imagens foram movida: s ou n ')
if resposta == 's':
    os.chdir('imagens_fits') #entra na pasta
    print os.listdir('.') #Lista a conteudo
 
 
    image_file = raw_input('Escreva o caminho para o arquivo fits: ')
 
    hdu_list = fits.open(image_file)
    #hdu_list.info()
 
    image_data = hdu_list[0].data
 
    print(type(image_data))
    print('O tamanho da img:', image_data.shape)
 
    hdu_list.close()
 
    image_data = fits.getdata(image_file)
    print(type(image_data))
    print(image_data.shape)
 
    plt.imshow(image_data, cmap='gray')
    plt.colorbar()
    plt.show()
 
 
    print(type(image_data.flat))
 
    histogram = plt.hist(image_data.flat)
    plt.show()
 
else:
    print('mova as imagens')