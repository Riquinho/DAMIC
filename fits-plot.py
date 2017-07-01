import numpy as np 
from scipy.stats import norm
import matplotlib
import matplotlib.pyplot as plt
import os
import glob
import sys

from astropy.utils.data import download_file
from astropy.io import fits

from astropy.modeling.models import Gaussian1D

from scipy.stats import linregress
from matplotlib import pyplot as pl



#Instrucoes de utilizacao do programa.
# python fits-plot.py s nomedoarquivo extensao

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

    #Histograma em escala log
    histogram1 = plt.hist(image_corte.flat, bins=2048)
    plt.yscale('log', nonposy='clip')
    plt.show()

    onedimension = image_corte.flatten() # transforma a matrix 2d em 1d 
    mu, std = norm.fit(onedimension) #media e desvio padrao

    print 'A matriz 1d do fits cortado:',onedimension

    #Formacao da gaussiana
    xp = np.linspace(onedimension.min(),onedimension.max(), 1000)
    p = norm.pdf(xp,mu,std)
    plt.plot(xp, p)
    plt.show()

    print 'Minimo:', image_corte.min()
    print 'Maximo:', image_corte.max()
    print 'Media:', image_corte.mean()
    print 'Sigma:', image_corte.std()

    #Somando colunas da matriz de corte (distribuicao binomial)
    soma_corte = image_corte.sum(axis=0)
    print (soma_corte)

    plt.plot(soma_corte)
    plt.show()

    #Regressao linear
    y= soma_corte
    x= range(len(soma_corte))
    m, b, R, p, SEm = linregress(x, y)

    def lin_regression(x, y):
    #Simple linear regression (y = m * x + b + error).
        m, b, R, p, SEm = linregress(x, y)

    # need to compute SEb, linregress only computes SEm
        n = len(x)
        SSx = np.var(x, ddof=1) * (n-1)  # this is sum( (x - mean(x))**2 )
        SEb2 = SEm**2 * (SSx/n + np.mean(x)**2)
        SEb = SEb2**0.5

        return m, b, SEm, SEb, R, p

    m, b, Sm, Sb, R, p = lin_regression(x, y)

    print('m = {:>.4g} +- {:6.4f}'.format(m, Sm))
    print('b = {:>.4g} +- {:6.4f}\n'.format(b, Sb))

    print('R2 = {:7.5f}'.format(R**2))
    print('p of test F : {:<8.6f}'.format(p))

    pl.plot(x,y, 'o')
    pl.xlim(0,None)
    pl.ylim(0, None)

    # desenho da recta, dados 2 pontos extremos
    # escolhemos a origem e o max(x)
    x2 = np.array([0, max(x)])

    pl.plot(x2, m * x2 + b, '-')

    # Anotacao sobre o grafico:
    ptxt = 'm = {:>.4g} +- {:6.4f}\nb = {:>.4g} +- {:6.4f}\nR2 = {:7.5f}'

    t = pl.text(0.5, 4, ptxt.format(m, Sm, b, Sb, R**2), fontsize=14)
    pl.show()
    

    arq = open("dados.txt", "w")
    arq.write("Minimo:")
    arq.write(str(image_corte.min()))
    arq.write("\n") #para inserir quebra de linha
    arq.write("Maximo:")
    arq.write(str(image_corte.max()))
    arq.close()

    
 
if not os.path.exists('imagens_fits'):
    os.makedirs('imagens_fits') #Cria a pasta

resposta = 'n'
while resposta == 'n':
    print('Por favor mova os arquivos fits para a pasta images_fits')
    resposta = sys.argv[1] #raw_input('As imagens foram movidas? [s/n] ')
    if resposta == 's':
        os.chdir('imagens_fits') #entra na pasta
        print("id: nome")
        dirlist = os.listdir('.')
        for i in range(len(dirlist)):
            print(i, ": ", dirlist[i]) #Lista a conteudo
        
        image_file = sys.argv[2] #raw_input('Escreva o nome ou a id do arquivo fits: ')
        if image_file.isdigit():
            image_file = dirlist[int(image_file)]
     
        hdu_list = fits.open(image_file)
        hdu_list.info()
    
        ext = int(sys.argv[3]) # int(raw_input("Qual extensao quer abrir? "))
        openHDU(hdu_list, ext)
    
        hdu_list.close()
