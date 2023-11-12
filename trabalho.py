import pandas as pd
from io import StringIO #finge qie é um arquivo, mas é string.
import matplotlib.pyplot as plt #graficos
import numpy as np #show de bola pra trabalhar
import streamlit as st #pagina

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

def tresPioresBairros():
    bairros = df['bairro'].value_counts()
    pioresBairrosRepetidos = bairros.tail(3).index.tolist() #os 3 quemais se repetem.
    return pioresBairrosRepetidos

def recorrenciaBairros():
    bairrosRepetidos = tresPrimeirosBairros()
    recorrencia = df[df['bairro'].isin(bairrosRepetidos)]['bairro'].value_counts() #aqui pegamos a quantidade de vezes que repeiu.
    return recorrencia.values

def recorrenciaPioresBairros():
    pioresBairrosRepetidos = tresPioresBairros()
    recorrencia = df[df['bairro'].isin(pioresBairrosRepetidos)]['bairro'].value_counts() #aqui pegamos a quantidade de vezes que repeiu.
    return recorrencia.values

def precoMedio():
    bairrosRepetidos = tresPrimeirosBairros()
    colunaPreco = df[df['bairro'].isin(bairrosRepetidos)] #Aqui transforma a coluna preço só dos 3 bairros selecionados, ai conseguimos tirar a media na linha de baixo usando groupby.
    preco = colunaPreco.groupby('bairro')['preco'].mean()
    preco = preco[bairrosRepetidos].values.astype(int) #preco medio apenas dos bairros que importam.
    return preco

def graficoBairros():
    bairros = tresPrimeirosBairros()
    tamanho = recorrenciaBairros()
    preco = precoMedio()
    
    fig, ax = plt.subplots()
    ax.pie(tamanho, labels=bairros)
    ax.set_title('Analise dos bairros mais vendidos')
    ax.legend(preco,title="Preço medio em R$:",loc="best")
    st.pyplot(fig)

    st.code('''
            def tresPrimeirosBairros():
                bairros = df['bairro'].value_counts()
                bairrosRepetidos = bairros.head(3).index.tolist()
                return bairrosRepetidos
            ''')
    
    st.code('''
            def recorrenciaBairros():
                bairrosRepetidos = tresPrimeirosBairros()
                recorrencia = df[df['bairro'].isin(bairrosRepetidos)]['bairro'].value_counts() 
                return recorrencia.values
            ''')
    st.code('''
            def precoMedio():
                bairrosRepetidos = tresPrimeirosBairros()
                colunaPreco = df[df['bairro'].isin(bairrosRepetidos)] 
                preco = colunaPreco.groupby('bairro')['preco'].mean()
                preco = preco[bairrosRepetidos].values.astype(int)
                return preco
            ''')


    bairros2 = tresPioresBairros()
    tamanho2 = recorrenciaPioresBairros()
    fig2, ax2 = plt.subplots()
    ax2.pie(tamanho2, labels=bairros2)
    ax2.set_title('Analise dos bairros menos vendidos')
    st.pyplot(fig2)
   
def preferenciaGaragem():
    garagem = df['garagem'].map({0: 'SEM', 1: 'COM'})
    garagem = garagem.value_counts()
    return garagem

def graficoGaragem():
    dados = preferenciaGaragem()
    valoresGaragem = dados.values
    labelsGaragem = dados.index

    fig, ax = plt.subplots()
    ax.bar(labelsGaragem, valoresGaragem)
    st.pyplot(fig)

    st.code(''' 
                def preferenciaGaragem():
                garagem = df['garagem'].map({0: 'SEM', 1: 'COM'})
                garagem = garagem.value_counts()
                return garagem
            ''')
    st.code(dados)
    st.code(''' 
                dados = preferenciaGaragem()
                valoresGaragem = dados.values
                labelsGaragem = dados.index

                fig, ax = plt.subplots()
                ax.bar(labelsGaragem, valoresGaragem)
            ''')

st.title("analise de dados")

graficoBairros()
graficoGaragem()