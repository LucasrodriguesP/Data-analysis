import pandas as pd
import matplotlib.pyplot as plt #graficos
import numpy as np #show de bola pra trabalhar
import streamlit as st #pagina

df = pd.read_csv('dados_imob.csv')

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

def preco_por_area():
    df['preco_m2'] = df['preco'] / df['m2'] #Calcula o preço por metro quadrado
    
    bairros_repetidos = df['bairro'].value_counts().head(10).index #obtém os 10 bairros mais repetidos

    df_filtrado = df[df['bairro'].isin(bairros_repetidos)] #filtra o df para incluir apenas os bairros mais repetidos

    media_por_bairro = df_filtrado.groupby('bairro')['preco_m2'].mean() #Agrupa pelos bairros e calcula a média do preço por metro quadrado

    # Cria um novo DataFrame com os resultados
    resultado = pd.DataFrame({
        'Bairros': media_por_bairro.index,
        'Preço/m2': media_por_bairro.values
    })

    resultado['Quantidade'] = df['bairro'].value_counts().reindex(resultado['Bairros']).values #Adiciona a coluna de quantidade de imóveis nos bairros

    resultado = resultado.sort_values(by='Quantidade', ascending=False) #Ordena pelos bairros mais repetidos

    # Remove a coluna de quantidade para ter o resultado final
    #resultado = resultado.drop('Quantidade', axis=1)
    
    resultado['Preço/m2'] = resultado['Preço/m2'].astype(int)# arredonda para duas casas decimais

    resultado = resultado.reset_index(drop=True) #Reinicia os índices do DataFrame

    #Código para deixar "Tabela de Preço/m2 em negrito e centralizado"
    #st.markdown("<h1 style='text-align: center; color: black;'><b>Tabela de Resultados</b></h1>", unsafe_allow_html=True)

    st.write("Tabela de preço por metro quadrado")

    st.table(resultado) #exibe a tabela na página

    st.code('''
            def preco_por_area():
                df['preco_m2'] = df['preco'] / df['m2'] #Calcula o preço por metro quadrado
                bairros_repetidos = df['bairro'].value_counts().head(10).index #obtém os 10 bairros mais repetidos
            
                df_filtrado = df[df['bairro'].isin(bairros_repetidos)] #filtra o df para incluir apenas os bairros mais repetidos

                media_por_bairro = df_filtrado.groupby('bairro')['preco_m2'].mean() #Agrupa pelos bairros e calcula a média do preço por metro quadrado

                # Cria um novo DataFrame com os resultados
                resultado = pd.DataFrame({
                    'Bairros': media_por_bairro.index,
                    'Preço/m2': media_por_bairro.values
                })

                resultado['Quantidade'] = df['bairro'].value_counts().reindex(resultado['Bairros']).values #Adiciona a coluna de quantidade de imóveis nos bairros

                resultado = resultado.sort_values(by='Quantidade', ascending=False) #Ordena pelos bairros mais repetidos

                # Remove a coluna de quantidade para ter o resultado final
                #resultado = resultado.drop('Quantidade', axis=1)
    
                resultado['Preço/m2'] = resultado['Preço/m2'].astype(int)# arredonda para duas casas decimais

                st.table(resultado)
    ''')


st.title("analise de dados")

graficoBairros()
graficoGaragem()
preco_por_area()