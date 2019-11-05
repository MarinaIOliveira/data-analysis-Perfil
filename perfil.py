#Importação das bibliotecas que serão utilizadas

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

#Base de dados com os perfis dos funcionários atuais da Trojan Technologies
perfis = "Perfis.json"

#Leitura do arquivo
dfPerfis = pd.read_json(perfis)

#Visualização do arquivo
#dfPerfis

#Número de instâncias no DataFrame
dfPerfis.shape

#Perfil Education

#Cada linha do arquivo possui uma lista de listas (Uma lista dentro de outra lista). Sendo assim foi necessário uma função para 
#realizar a concatenação de cada lista. Essa concatenação será adicionada na listasEducation. 
#Tornando essas listas em apenas uma.

#Função para concatenação das listas
def concatenaEducation(listas):
    listasEducations = []
    for i in  range(len(listas)):
        #Concatenação
        listasEducations = listasEducations + listas[i]
    return listasEducations

#Chamada da Função concatenaEducation, enviando a coluna 'education'
educationPerfis = pd.DataFrame(concatenaEducation(dfPerfis.education))
#Visualização da tabela Education
educationPerfis.head()

#Tratamento dos dados
#Valores nulos
educationPerfis = educationPerfis.dropna()

#Após concatenação dos dados observou-se que a coluna degree possuia o texto "Nome do diploma\n" antes da informação, 
#confundindo-se então a visualização. Sendo assim, utilizou-se o 'replace' para substituir a frase ('').
educationPerfis = educationPerfis.replace('Nome do diploma\n','',regex=True)

#A mesma situação ocorreu com a coluna 'major', a qual apresentava o texto "Área de estudo\n".
educationPerfis = educationPerfis.replace('Área de estudo\n','',regex=True)

#Após concatenação dos dados observou-se que algumas informações eram iguais porém com a escrita diferente, sendo necessário
#normalizá-las para não influenciarem na contagem da análise
educationPerfis = educationPerfis.replace('Colégio Cotemig','COTEMIG',regex=True)
educationPerfis = educationPerfis.replace('Colégio COTEMIG','COTEMIG',regex=True)
educationPerfis = educationPerfis.replace('Faculdade Cotemig','COTEMIG',regex=True)

educationPerfis = educationPerfis.replace('Centro Universitário de Belo Horizonte - UNI-BH','UNI-BH',regex=True)
educationPerfis = educationPerfis.replace('Uni-BH','UNI-BH',regex=True)

#np.unique(educationPerfis)

#Visualização da tabela Education
#Visualizando apenas as 5 primeiras linhas (.head())
educationPerfis.head()

#School
educationPerfis.groupby('school').count()

#Perfil Experiences

#Função para concatenação das listas
def concatenaExperiences(listas):
    listasExperiences = []
    for i in  range(len(listas)):
        #Concatenação
        listasExperiences = listasExperiences + listas[i]
    return listasExperiences

#Chamada da Função 
experiencesPerfis = pd.DataFrame.from_dict(concatenaExperiences(dfPerfis.experiences))

#Visualização da tabela Experiences
#Visualizando apenas as 5 primeiras linhas (.head())
experiencesPerfis.head()

#Após concatenação dos dados observou-se que algumas informações eram iguais porém com a escrita diferente, sendo necessário
#normalizá-las para não influenciarem na contagem da análise
experiencesPerfis = experiencesPerfis.replace('Belo Horizonte/MG','Belo Horizonte, Brasil',regex=True)
experiencesPerfis = experiencesPerfis.replace('belo horizonte','Belo Horizonte, Brasil',regex=True)
experiencesPerfis = experiencesPerfis.replace('Belo Horizonte, Minas Gerais','Belo Horizonte, Brasil',regex=True)
experiencesPerfis = experiencesPerfis.replace('belo Horizonte','Belo Horizonte, Brasil',regex=True)
experiencesPerfis = experiencesPerfis.replace('Belo Horizonte Area, Brazil','Belo Horizonte, Brasil',regex=True)
experiencesPerfis = experiencesPerfis.replace('Belo Horizonte','Belo Horizonte, Brasil',regex=True)
experiencesPerfis = experiencesPerfis.replace('Belo Horizonte e Região,Brasil e Região,Brasil','Belo Horizonte, Brasil',regex=True)
experiencesPerfis = experiencesPerfis.replace('BrasilBrasil e Região,Brasil e Região, Brasil','Belo Horizonte, Brasil',regex=True)
experiencesPerfis = experiencesPerfis.replace('BrasilBrasil e Região,Brasil e Região,Brasil','Belo Horizonte, Brasil',regex=True)
experiencesPerfis = experiencesPerfis.replace('São Paulo Area, Brazil','São Paulo, Brasil',regex=True)
experiencesPerfis = experiencesPerfis.replace('São Paulo, São Paulo','São Paulo, Brasil',regex=True)
experiencesPerfis = experiencesPerfis.replace('São Paulo','São Paulo, Brasil',regex=True)
experiencesPerfis = experiencesPerfis.replace('São Paulo e Região, Brasil e Região, Brasil','São Paulo, Brasil',regex=True)
experiencesPerfis = experiencesPerfis.replace('São Paulo e Região, Brasil, Brasil','São Paulo, Brasil',regex=True)
experiencesPerfis = experiencesPerfis.replace('Manaus Area, Brazil','Manaus e Região, Brasil',regex=True)
experiencesPerfis = experiencesPerfis.replace('Manaus','Manaus e Região, Brasil',regex=True)
experiencesPerfis = experiencesPerfis.replace('Manaus e Região, Brasil e Região, Brasil','Manaus, Brasil',regex=True)

#Valores nulos
experiencesPerfis = experiencesPerfis.dropna()

experiencesPerfis.head()

#Position
experiencesPerfis.groupby('position').count()

#Experiences Perfis by Position
#Gráfico não ficou bom
experiencesPerfis.groupby('position').count().plot(kind='bar', color='black', figsize=(100,10))

#location
experiencesPerfis.groupby('location').count()

#Perfil Gender

genderPerfis = dfPerfis.gender
#Visualização da tabela Gender
#genderPerfis
genderPerfis.head()

#Valores nulos
genderPerfis = genderPerfis.dropna(how='all')

#Visualização da tabela Gender
#Visualizando apenas as 5 primeiras linhas (.head())
#genderPerfis.head()

#Contagem dos valores 
genderPerfis.value_counts()
#genderPerfis.describe()

descricao = ['FEMALE', 'MALE', 'NA']

value_countsPerfis = [39,65,7]

plt.pie(value_countsPerfis, labels=descricao, autopct='%1.1f%%')
plt.title('Gênero')
plt.show()

#Perfil Languages

#Função para Concatencação das listas
def concatenaLanguages(listas):
    listasLanguages = []
    for i in (listas):
        if not type(i) is float:
            #A concatenação só é realizada para listas que não são do tipo "float", para essa tabela, foi necessário realizar uma 
            #condição para verificação.
            for x in i:
                listasLanguages.append(x)
    return listasLanguages
                       
#Chamada da Função
languagesPerfis = pd.DataFrame(concatenaLanguages(dfPerfis.languages))

#Visualização da tabela Languages
#languagesPerfis

#Visualização da tabela Languages
#Visualizando apenas as 5 primeiras linhas (.head())
#languagesPerfis.head()

#Após concatenação dos dados observou-se que a coluna name possuia o texto "Idioma\n" antes da informação, 
#confundindo-se então a visualização. Sendo assim, utilizou-se o 'replace' para substituir a frase ('').
languagesPerfis = languagesPerfis.replace('Idioma\n','',regex=True)


#Após concatenação dos dados observou-se que algumas informações eram iguais porém com a escrita diferente, sendo necessário
#normalizá-las para não influenciarem na contagem da análise
languagesPerfis = languagesPerfis.replace('Inglês - Intermediário - em curso','Inglês',regex=True)
languagesPerfis = languagesPerfis.replace('Inglês - Certificação TOEIC','Inglês',regex=True)
languagesPerfis = languagesPerfis.replace('Inglês médio ','Inglês',regex=True)
languagesPerfis = languagesPerfis.replace('Inglês(1100-1500)','Inglês',regex=True)#Não funcionou
languagesPerfis = languagesPerfis.replace('English','Inglês',regex=True)

languagesPerfis = languagesPerfis.replace('Portuguese','Português',regex=True)
languagesPerfis = languagesPerfis.replace('Portugais','Português',regex=True)

languagesPerfis = languagesPerfis.replace('Spanish','Espanhol',regex=True)


languagesPerfis = languagesPerfis.replace('French','Francês',regex=True)
languagesPerfis = languagesPerfis.replace('Français','Francês',regex=True)

languagesPerfis = languagesPerfis.replace('Italian','Italiano',regex=True)
languagesPerfis = languagesPerfis.replace('Italianoo','Italiano',regex=True)


#Valores nulos
languagesPerfis = languagesPerfis.dropna()

#Languages
languagesPerfis.groupby('name').count().plot(kind='bar', color='black')

#Foi realizado o agrupamento(groupby) dos valores a fim apresentar todas as linguagens preenchidas
languagesPerfis.groupby('name').count()

#Analisando as 3 linguas mais faladas
#Gráfico referente as 3 linguas mais faladas
languagesPerfis['name'].value_counts().head(3).plot(kind='bar', color='black')
plt.title('Linguagens mais populares')
plt.xlabel('Lnguages')
plt.show()

#Nível de Proficiency em geral das linguagens
languagesPerfis.groupby('proficiency').count()

descricao = ['Fluente', 'Nível Avançado', 'Nível Básico', 'Nível Básico', 'Nível Intemediário']

value_countsProficiency = [78,42,16,26,26]

plt.pie(value_countsProficiency, labels=descricao, autopct='%1.1f%%')
plt.title('Proficiência')
plt.show()

#Perfil Skill

#Função para Concatencação das listas
def concatenaSkill(listas):
    listasSkills = []
    for i in (listas):
        #A concatenação só é realizada para listas que não são do tipo "float", para essa tabela, foi necessário realizar uma 
        #condição para verificação.
        if not type(i) is float:
            for x in i:
                listasSkills.append(x)
    return listasSkills
         
#Chamada da Função
skillsPerfis = pd.DataFrame(concatenaSkill(dfPerfis.skills))

#Visualização da tabela Skills
#Visualizando apenas as 5 primeiras linhas (.head())
skillsPerfis.head()

#Valores nulos
skillsPerfis = skillsPerfis.dropna()

skillsPerfis.head()

#Após concatenação dos dados observou-se que algumas informações eram iguais porém com a escrita diferente, sendo necessário
#normalizá-las para não influenciarem na contagem da análise
skillsPerfis = skillsPerfis.replace('Empresas startups','Startup',regex=True)
skillsPerfis = skillsPerfis.replace('Start-ups','Startup',regex=True)
skillsPerfis = skillsPerfis.replace('Entrepreneurship','Empreendedorismo',regex=True)

skillsPerfis.head()

skillsPerfis.head()

skillsPerfis.groupby('name').count().plot(kind='bar', color='black', figsize=(50,10))



sns.heatmap(dfMatriz, annot=True)