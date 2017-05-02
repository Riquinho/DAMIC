import numpy as np 
import matplotlib
import matplotlib.pyplot as plt
import os
import glob
 
from astropy.utils.data import download_file
from astropy.io import fits
 
def openHDU(hdulist, ext):
    image_data = hdu_list[ext].data
  
    print 'O tipo de imagem:', type(image_data)
    print 'O tamanho da img:', image_data.shape
     
    image_data = fits.getdata(image_file)
 
    print(image_data)
 
    plt.imshow(image_data, cmap='gray', clim=(4000, 5000))
    plt.xlim(100, 8544)
    plt.colorbar()
    plt.show()
 
    print 'Minimo:', image_data.min()
    print 'Maximo:', image_data.max()
    print 'Media:', image_data.mean()
    print 'Sigma:', image_data.std()
 
    print(type(image_data.flat))
 
    #Histograma
    histogram = plt.hist(image_data.flat, bins=1000)
    plt.show()
 
    #Historgrama em escala logaritima" 
    histogram1 = plt.hist(image_data.flat, bins=1000)
    plt.yscale('log', nonposy='clip')
    plt.show()
  
if not os.path.exists('imagens_fits'):
    os.makedirs('imagens_fits') #Cria a pasta
  
print('Por favor mova os arquivos fits para a pasta images_fits')
resposta = raw_input('as imagens foram movida: (s ou n) ')
if resposta == 's':
    os.chdir('imagens_fits') #entra na pasta
    print(os.listdir('.')) #Lista a conteudo 
    image_file = raw_input('Escreva o caminho para o arquivo fits: ')
  
    hdu_list = fits.open(image_file)
    hdu_list.info()
 
    ext = int(input("Qual extensao quer abrir? "))
    openHDU(hdu_list, ext)
 
    hdu_list.close()
  
else:
    print('mova as imagens')