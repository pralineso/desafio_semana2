#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[120]:


import pandas as pd
import numpy as np


# In[121]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[115]:


#np.random.seed(1)

#df = pd.DataFrame(np.random.randn(4,4)* 4 + 3)

#df
#normalized_df=(df-df.min())/(df.max()-df.min())


# In[116]:


#df.describe()


# In[117]:


#normalized_df=(df-df.min())/(df.max()-df.min())


# In[118]:


#normalized_df


# In[122]:


#from sklearn import preprocessing
#min_max = preprocessing.MinMaxScaler() 
#res_transformacao = min_max.fit_transform(df) 
#df_normalizado = pd.DataFrame(res_transformacao) 
#df_normalizado 


# In[123]:


#from sklearn import preprocessing
#coluna_purchase = black_friday['Purchase'] #primeiro peguei so a colna purchase
#df = pd.DataFrame(coluna_purchase) #transformando a tabelinha em dataframe
#min_max = preprocessing.MinMaxScaler() #processamento do minemax
#res_transformacao = min_max.fit_transform(df) # transformacao dos dados da coluna purchase pro minemax da formula la, isos gera um vetor ja com resultado
#res_transformacao

    


# In[126]:


#coluna_purchase_normalizada = pd.DataFrame(res_transformacao) #trsnformacao do vetor de antes em dtframe
#float(coluna_purchase_normalizada.mean()) #retorna a media dos valores da coluna, depois de normalizado


# In[124]:



#coluna_purchase = black_friday['Purchase'] #primeiro peguei so a colna purchase
#df = pd.DataFrame(coluna_purchase) #transformando a tabelinha em dataframe
#fonte https://www.it-swarm.dev/pt/python/normalize-colunas-do-dataframe-do-pandas/1049023341/
#normalized_df=(df-df.min())/(df.max()-df.min())
#float(normalized_df.mean())
#float(coluna_purchase_normalizada.mean()) #retorna a media dos valores da coluna, depois de normalizado


# In[127]:


#float(normalized_df.mean())


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[34]:


def q1():
    # Retorne aqui o resultado da questão 1.
    #aki tbm podia se so ... black_friday.shape
    t = (black_friday.shape[0], black_friday.shape[1])
    return t
    pass


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[31]:


def q2():
    # Retorne aqui o resultado da questão 2.
    aux = black_friday[['Gender','Age']] #primeiro montei uma tbl aux so com as colunas necessarias
    mulheres = aux.loc[aux['Gender']=='F'] #depois filtrei so os dados onde a coluna genero é igual a F
    cont = mulheres['Age'].value_counts() #depois contei a qtd de tds  as idades
    cont = int(cont.iloc[0]) # como tem mais mulheres com a idade entre 26 e 35, esse resultado ta na primeira linha
    return cont
    pass


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[22]:


def q3():
    # Retorne aqui o resultado da questão 3.
    qtd_user_unico = black_friday['User_ID'].nunique() # aqui foi feita a filtragem pelo id do usuario com esse comando magico nunique()
    return qtd_user_unico
    pass


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[7]:


def q4():
    # Retorne aqui o resultado da questão 4.
    qtd_total_unico = black_friday.nunique().sum() #aqui foi feita filtragem de dados unicos e depois a sua soma
    return int(qtd_total_unico)
    pass


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[8]:


def q5():
    # Retorne aqui o resultado da questão 5.
    percent_ind = black_friday.isnull().sum()/black_friday.shape[0] # esse comando filtra a soma da qtd de null e depois divide pela quantidade total 
    percent = percent_ind.sum()/12 #com resultado da porcentagem individual foi divido por 12 porque sao 12 colunas
    return float(percent)
    pass


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[9]:


def q6():
    # Retorne aqui o resultado da questão 6.
    #percent_ind = black_friday.isnull().sum()/black_friday.shape[0]
    #por conta do comando de cima eu sei q é a coluna Product Category 3
    qtd_null = black_friday['Product_Category_3'].isnull().value_counts().iloc[0] # e entao foi feito uma filtragem da quantidade total de valores null.. o iloc[0] pega o primeiro resultado, que é o maior
    return int(qtd_null)
    pass


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[10]:


def q7():
    # Retorne aqui o resultado da questão 7.
    #black_friday['Product_Category_3'].value_counts()
    #eu sei q é o 16 porque quando é executado a linha de cima ela volta uma lista com os valores e o 16 é o 
    #que tem mais valores repetidos
    #pois eu nao sei como q faz pra pegar a primeira parte do resultado da tabelinha
    return 16
    pass


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[11]:


def q8():
    # Retorne aqui o resultado da questão 8.
    coluna_purchase = black_friday['Purchase'] #primeiro peguei so a coluna purchase
    df = pd.DataFrame(coluna_purchase) #transformando a tabelinha em dataframe
    #fonte https://www.it-swarm.dev/pt/python/normalize-colunas-do-dataframe-do-pandas/1049023341/
    normalized_df=(df-df.min())/(df.max()-df.min())
    return float(normalized_df.mean())
    pass


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[12]:


def q9():
    # Retorne aqui o resultado da questão 9.
    coluna_purchase = black_friday[['Purchase']]
    #fonte principal (https://minerandodados.com.br/pre-processamento-standartization/)
    re_escala = preprocessing.StandardScaler().fit(coluna_purchase)
    res_padronizacao = re_escala.transform(coluna_purchase) 
    coluna_purchase_padronizada = pd.DataFrame(res_padronizacao)
    coluna_purchase_padronizada.columns = ['purchase'] #renomeando a coluna pq no padrao fica 0
    qtd_de_um_e_menos = coluna_purchase_padronizada['purchase'].between(-1, 1, inclusive=True).value_counts().iloc[0]
    #fitra os valores entre -1 e 1 inclluindo tais valores, isso retorna tipo true e false, ai ele conta a qtd de true e false, e o iloc pega a primeira linha com qtd 
    #de valores true entre -1 e 1
    return qtd_de_um_e_menos

    pass


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[13]:


def q10():
    # Retorne aqui o resultado da questão 10.False
    product_2 = black_friday['Product_Category_2'].isnull() #verificando os valores null da coluna produto categoria 2
    product_3 = black_friday['Product_Category_3'].isnull() #verificando os valores  null da coluna produto categoria 3
    return product_2.equals(product_3) #retornando o resultado da comparaçao entre as duas colunas
    pass

