# data-analysis-Perfil
Análise de dados para entender melhor o perfil das futuras contratações 

**Trabalho Prático - Introdução às Linguagens Estatísticas**

**Introdução**
A fim de entender melhor o perfil das futuras contratações da Trojan Technologies SA e verificar se o as contrações anteriores seguiam um perfil homogênio, Aquiles contratou um cientista de dados para analisar a base de dados atual da empresa e obter insights e respostas.

**Implementação**
Cada linha do arquivo "Perfis.json" possui uma lista de listas (Uma lista dentro de outra lista). Sendo assim foi necessário uma função para realizar a concatenação de cada lista tornando essas listas em apenas uma.

A função de concatenação recebe como parametro uma coluna do DataFrame. Possui uma lista vazia, a qual será adicionado a concatenação das listas da coluna desejada. É utilizado um laço de repeticação for, o qual possui um index 'i' percorre até o final da "listas" recebida como parâmetro. Após a concatenação a função retorna a lista, inicialmente vazia, qua agora possui o resultado da concateção das listas.

Para limpeza e preparação dos dados, primeiramente foi utilizado o .dropna() para realizar a remoção dos valores nulos pertencentes nas tabelas. Observou-se também que em algumas tabelas, algumas colunas possuia textos antes da informação desejada, confundindo-se então a visualização. Sendo assim, utilizou-se o 'replace' para substituir/retirar o texto ('').

**Resultados**
Foi realizado a análise de cada tabela separadamente, a fim de conhecer suas informações e assim, ser possibilitando a junção dos dados formando o melhor perfil para a Trojan Technologies SA baseado em sua base de dados. Foi realizado a contagem de cada habilidade, linguagem e diferencial de cada tabela, apresentando assim as características mais populares dos profissionais.

