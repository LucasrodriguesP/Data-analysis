import pandas as pd
from io import StringIO #finge qie é um arquivo, mas é string.
import matplotlib.pyplot as plt #graficos
import numpy as np #show de bola pra trabalhar




unicode = ['utf-8', 'latin1', 'iso-8859-1'] # Aqui teve bug com o unicode, esse for com try catch testa esses 3 tipos diferentes.
for unicode in unicode:
    try:
        with open('kgz7s-3aihd.csv', 'rb') as file:
            auxiliar = file.read()
            auxiliar = auxiliar.decode(unicode)
            df = pd.read_csv(StringIO(auxiliar)) #aqui fingimos que o auxiliar é um arquivo e criamos um dataframe.
    except UnicodeDecodeError:
        continue



def tresPrimeirosBairros():

    bairros = df['bairro'].value_counts()
    bairrosRepetidos = bairros.head(3).index.tolist() #os 3 quemais se repetem.
    return bairrosRepetidos


def recorrenciaBairros():
    bairros = df['bairro'].value_counts()
    bairrosRepetidos = bairros.head(3).index.tolist() #os 3 quemais se repetem.
    recorrencia = df[df['bairro'].isin(bairrosRepetidos)]['bairro'].value_counts() #aqui pegamos a quantidade de vezes que repeiu.
    return recorrencia.values

def precoMedio():
    bairros = df['bairro'].value_counts()
    bairrosRepetidos = bairros.head(3).index.tolist() #os 3 quemais se repetem.
    colunaPreco = df[df['bairro'].isin(bairrosRepetidos)] #Aqui transforma a coluna preço só dos 3 bairros selecionados, ai conseguimos tirar a media na linha de baixo usando groupby.
    preco = colunaPreco.groupby('bairro')['preco'].mean()
    preco = preco[bairrosRepetidos].values.astype(int) #preco medio apenas dos bairros que importam.
    return preco

def graficoBairros():
    bairros = tresPrimeirosBairros()
    tamanho = recorrenciaBairros()
    preco = precoMedio()
    

    ax = plt.subplots()
    ax.pie(tamanho, labels=bairros)
    ax.set_title('Analise dos bairros mais vendidos')
    ax.legend(preco,title="Preço medio em R$:",loc="best")
    plt.show()

graficoBairros()
