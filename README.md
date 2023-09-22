# Predictive_Churn

Este projeto de classificação de churn visa aplicar técnicas de Ciência de Dados e Machine Learning para identificar clientes em risco de abandono, auxiliando a empresa a melhorar a retenção e maximizar a receita.

| :placard: Vitrine.Dev |https://cursos.alura.com.br/vitrinedev/paulo-f-luiz/project/Alura_Challenge_Novexus/12180243     |
| -------------  | --- |
| :sparkles: Nome        | **Predictive_Churn**
| :label: Tecnologias | python, pandas, scikit-learn, matplotlib, plotly
| :rocket: URL         |https://novexus.streamlit.app/
| :fire: Desafio     | [Challenge Dados Alura](https://www.alura.com.br/challenges/dados-2?host=https://cursos.alura.com.br)

<!-- Inserir imagem com a #vitrinedev ao final do link -->
![](https://github.com/pfluiz/Alura_Challenge_Novexus/blob/a557fabd0e6154e7425cba12046b1fa456f219a8/Logo%20(5).png#vitrinedev)

# Descrição do Projeto

Este projeto busca entender e analisar o fenômeno de "Churn" de clientes em um conjunto de dados obtidos através de uma API. O objetivo é identificar padrões, criar visualizações e aplicar técnicas de pré-processamento para preparar os dados para modelagem. O projeto foi dividido em vários desafios para tornar a análise mais estruturada e eficaz.

# SEMANA 1 - RESUMO

### 1. Entender quais informações o conjunto de dados possui
- **Atividades**: 
    - Carregamento do conjunto de dados para entender sua estrutura e os tipos de dados.
    - Análise exploratória para identificar colunas, tipos de dados e valores ausentes.
    - Resumo estatístico para ter uma visão geral das métricas distribucionais.

### 2. Criar visualizações relevantes em relação ao Churn
- **Atividades**: 
    - Utilização de gráficos de barra e boxplot para visualizar a distribuição das classes e a relação com outras variáveis.
   
### 3. Aplicar encoding adequado nos dados
- **Atividades**: 
    - Identificação das variáveis categóricas que necessitam de encoding.
    - Aplicação da técnica One-Hot Encoding para transformar as variáveis categóricas em um formato que possa ser alimentado em modelos de Machine Learning.

### 4. Analisar a correlação das variáveis
- **Atividades**: 
    - Utilização de métodos estatísticos para calcular a correlação entre as variáveis.
    
## Resultados da Semana

O resultado deste projeto foi a criação de um DataFrame contendo apenas as características definidas pelo método chi2. Estes dados serão utilizados para a construção dos modelos de Machine Learning na próxima semana.


# SEMANA 2 - RESUMO

## Verificação de Balanceamento da Variável Target

A variável target foi minuciosamente avaliada para verificar se estava balanceada. Identificou-se um desbalanceamento no conjunto de dados. Para abordar essa questão, o método de Under Sampling foi aplicado, conforme orientações presentes no artigo “Lidando com o desbalanceamento de dados”.

## Métrica a ser Otimizada: Recall

Escolheu-se o Recall como a métrica ideal para ser otimizada. A justificativa para a utilização dessa métrica centra-se na sua capacidade de identificar verdadeiros positivos. No contexto do projeto, que envolve a classificação de churn, é crucial minimizar o número de falsos negativos. Ou seja, queremos evitar a situação em que o modelo prevê que um cliente não irá abandonar o serviço quando, na realidade, ele vai. Isso é especialmente crítico em um cenário de churn, onde perder um cliente pode ter implicações financeiras significativas para o negócio.

## Modelos de Machine Learning Criados

Durante esta fase, foram implementados três modelos diferentes para solucionar o problema de classificação: 

1. Random Forest
2. Regressão Logística
3. XGBoost

A implementação de múltiplos modelos permitiu uma experimentação robusta e uma análise mais profunda das métricas de classificação.

## Escolha do Melhor Modelo

Os três modelos tiveram uma performance superior quando aplicados ao conjunto de dados balanceado com Under Sampling. 

## Otimização do Melhor Modelo

Foi realizado um Grid Search em cada um dos modelos. Esta otimização resultou em uma leve melhoria do modelo de Regressão Logística.

## Salvamento do Modelo

Finalmente, o modelo de Regressão Logística otimizado foi salvo utilizando a biblioteca `pickle`, permitindo sua reutilização futura para previsões mais precisas em novos conjuntos de dados.

Este resumo serve como um registro das atividades realizadas durante a segunda semana do projeto de Data Science e será anexado ao arquivo README no repositório do GitHub.


