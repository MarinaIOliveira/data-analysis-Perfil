#Importação das bibliotecas que serão utilizadas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pandas import DataFrame
%matplotlib inline

#Base é a matriz de similaridade entre os cursos
matrizSimilaridade = "matriz_similaridade_cursos.csv"

#Leitura do arquivo
dfMatriz = pd.read_csv(matrizSimilaridade)

#dfMatriz.head()


linha = ['Administração','Agronegócio','Agronomia','Arquitetura e Urbanismo','Bioquímica', 'Ciência da Computação','Ciência e Tecnologia de Laticínios'
'Ciências Biológicas', 'Ciências Contábeis', 'Ciências Econômicas', 'Ciências Sociais','Comunicação Social','Cooperativismo',
'Dança','Direito','Economia Domestica', 'Educação Física','Educação do Campo', 'Enfermagem', 'Engenharia Agrícola e Ambiental', 
'Engenharia Ambiental', 'Engenharia Civil', 'Engenharia Elétrica', 'Engenharia MecÂnica','Engenharia Química', 'Engenharia de Agrimensura e Cartográfica',
'Engenharia de Alimentos', 'Engenharia de Produção', 'Física', 'Geografia','História', 'Letras', 'Matemática', 'Medicina', 
'Medicina Veterinária', 'Nutrição', 'Pedagogia','Química', 'Secretariado Executivo Trilíngue', 'Serviço Social', 'Zootecnia']

matrizSimilaridade = "matriz_similaridade_cursos.csv"

#Leitura do arquivo
dfMatriz = pd.read_csv(matrizSimilaridade)

df = DataFrame(dfMatriz, index=linha, columns=linha)

df = pd.DataFrame(dfMatriz)