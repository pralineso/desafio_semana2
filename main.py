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

# In[4]:


import pandas as pd
import numpy as np


# In[5]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[43]:


#Q1
#n_observacoes = (black_friday.shape[0])
#n_colunas = (black_friday.shape[1])
#tupla = (n_observacoes,n_colunas)
#tupla

#Q2
#Gender,Age
#aux = black_friday[['Gender','Age']]
#mulheres = aux.loc[aux['Gender']=='F']
#cont = mulheres['Age'].value_counts()
#cont = cont.iloc[0]


#Q3
#qtd_user_unico = black_friday['User_ID'].nunique()
#qtd_user_unico

#Q4
#black_friday.nunique()
#qtd_total_unico = black_friday.nunique().sum()
#type(qtd_total_unico)

#Q5
#black_friday.isna().sum() / black_friday.shape[0]
#percent_ind = black_friday.isnull().sum()/black_friday.shape[0]
#percent = percent_ind.sum()/12
#float(percent)

#Q6
#t = black_friday['Product_Category_3'].isnull().value_counts()
type(373299)
#Q7
#black_friday['Product_Category_3'].value_counts()
# 16.0    32148
#32148

#Q10
#product_2 = black_friday['Product_Category_2'].isnull()
#product_3 = black_friday['Product_Category_3'].isnull()
#product_2.equals(product_3)
#product_2



# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[34]:


def q1():
    # Retorne aqui o resultado da questão 1.
    t = (black_friday.shape[0], black_friday.shape[1])
    return t
    pass


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[31]:


def q2():
    # Retorne aqui o resultado da questão 2.
    aux = black_friday[['Gender','Age']]
    mulheres = aux.loc[aux['Gender']=='F']
    cont = mulheres['Age'].value_counts()
    cont = int(cont.iloc[0])
    return cont
    pass


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[22]:


def q3():
    # Retorne aqui o resultado da questão 3.
    qtd_user_unico = black_friday['User_ID'].nunique()
    return qtd_user_unico
    pass


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[7]:


def q4():
    # Retorne aqui o resultado da questão 4.
    qtd_total_unico = black_friday.nunique().sum()
    return int(qtd_total_unico)
    pass


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[8]:


def q5():
    # Retorne aqui o resultado da questão 5.
    black_friday.isna().sum() / black_friday.shape[0]
    percent_ind = black_friday.isnull().sum()/black_friday.shape[0]
    percent = percent_ind.sum()/12
    return float(percent)
    pass


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[9]:


def q6():
    # Retorne aqui o resultado da questão 6.
    pass


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[10]:


def q7():
    # Retorne aqui o resultado da questão 7.
    return 16
    pass


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[11]:


def q8():
    # Retorne aqui o resultado da questão 8.
    pass


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[12]:


def q9():
    # Retorne aqui o resultado da questão 9.
    pass


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[13]:


def q10():
    # Retorne aqui o resultado da questão 10.False
    pass

