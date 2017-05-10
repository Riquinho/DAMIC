import numpy as np 
from scipy.stats import norm
import matplotlib
import matplotlib.pyplot as plt
import os
import glob

from astropy.utils.data import download_file
from astropy.io import fits

from astropy.modeling.models import Gaussian1D

def openHDU(hdulist, ext):
    image_data = hdu_list[ext].data

    #Exibe a image fits
    plt.imshow(image_data, cmap='gray', clim=(4000, 5000))
    plt.xlim(100, 8544)
    plt.colorbar()
    plt.show()

    print(type(image_data.flat))
    print(image_data) # Exibe a matriz 2D numpy do fits

    #Histograma
    histogram = plt.hist(image_data.flat, bins=2048)
    plt.show()

    #Histograma em escala log
    histogram1 = plt.hist(image_data.flat, bins=2048)
    plt.yscale('log', nonposy='clip')
    plt.show()

    onedimension = image_data.flatten() # transforma a matrix 2d em 1d 
    mu, std = norm.fit(onedimension) #media e desvio padrao

    print 'A matriz 1d do fits:',onedimension

    #Formacao da gaussiana
    xp = np.linspace(onedimension.min(),onedimension.max(), 1000)
    p = norm.pdf(xp,mu,std)
    plt.plot(xp, p)
    plt.show()
    

    print(type(image_data))
    print('O tamanho da img:', image_data.shape)

    print 'Minimo:', image_data.min()
    print 'Maximo:', image_data.max()
    print 'Media:', image_data.mean()
    print 'Sigma:', image_data.std()

    #Lado esquerdo do fits.
    #div = np.resize(image_data, (4298,4272))
    #print div
    #plt.imshow(div, cmap='gray')
    #plt.xlim(100, 4272)
    #plt.colorbar()
    #plt.show()

    #Recorte do fits
    corte= int(raw_input("Digite a primeira coordenada de corte do eixo y"))
    corte2= int(raw_input("Digite a segunda coordenada de corte do eixo y")) +1
    corte3= int(raw_input("Digite a primeira coordenada de corte do eixo x"))
    corte4= int(raw_input("Digite a segunda coordenada de corte do eixo x")) +1

    image_corte = image_data[corte:corte2,corte3:corte4]

    print (image_corte)

    #histograma imagem cortada
    histogram = plt.hist(image_corte.flat, bins=2048)
    plt.show()






    minInt = int(raw_input("Entre com o valor minimo de intensidade desejada: "))
    maxInt = int(raw_input("Entre com o valor maximo de intensidade desejada: "))

    trim = 1.0-float(raw_input("Entre com a porcentagem desejada de plotagem: "))

    width = image_data.shape[1]
    trimPixel = width*trim

    plt.imshow(image_data, cmap='gray', clim=(minInt, maxInt))
    plt.xlim(trimPixel/2.0, width-trimPixel/2.0)
    plt.colorbar()
    plt.show()
 
if not os.path.exists('imagens_fits'):
    os.makedirs('imagens_fits') #Cria a pasta

resposta = 'n'
while resposta == 'n':
    print('Por favor mova os arquivos fits para a pasta images_fits')
    resposta = raw_input('As imagens foram movidas? [s/n] ')
    if resposta == 's':
        os.chdir('imagens_fits') #entra na pasta
        print("id: nome")
        dirlist = os.listdir('.')
        for i in range(len(dirlist)):
            print(i, ": ", dirlist[i]) #Lista a conteudo
        
        image_file = raw_input('Escreva o nome ou a id do arquivo fits: ')
        if image_file.isdigit():
            image_file = dirlist[int(image_file)]
     
        hdu_list = fits.open(image_file)
        hdu_list.info()
    
        ext = int(raw_input("Qual extensao quer abrir? "))
        openHDU(hdu_list, ext)
    
        hdu_list.close()
