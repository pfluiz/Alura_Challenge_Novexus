from imblearn.under_sampling import RandomUnderSampler
from pandas import json_normalize
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import recall_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
import plotly.express as px
import random
import seaborn as sns
import xgboost as xgb
import joblib
from joblib import load
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Carregar o modelo treinado
model = joblib.load('lgbm_final_model.pkl')

# Título do app
st.title('Previsor de Rotatividade')


# Coletar dados do usuário usando caixas de rádio
internet_seguranca_online = st.radio('Cliente tem Segurança Online?', ('Sim', 'Não'))
# Convertendo a resposta em binário
internet_seguranca_online = 1 if internet_seguranca_online == 'Sim' else 0

internet_suporte_tecnico = st.radio('Cliente tem Suporte Técnico?', ('Sim', 'Não'))
# Convertendo a resposta em binário
internet_suporte_tecnico = 1 if internet_suporte_tecnico == 'Sim' else 0

# Coletar a permanência como um número inteiro
permanencia = st.text_input('Há quanto tempo o cliente está conosco? (em meses):')
permanencia_0_5 = 0
permanencia_61_70 = 0
permanencia_71_80 = 0
# Verificar qual variável de permanência deve ser ativada
if permanencia:
    permanencia = int(permanencia)
    if 0 <= permanencia <= 5:
        permanencia_0_5 = 1
    elif 61 <= permanencia <= 70:
        permanencia_61_70 = 1
    elif 71 <= permanencia <= 80:
        permanencia_71_80 = 1

# Inicializar as variáveis com 0
Conta_Contrato_MesAMes = 0
Conta_Contrato_UmAno = 0
Conta_Contrato_DoisAnos = 0

# Usar um único selectbox para capturar o tipo de contrato
tipo_contrato = st.selectbox(
    'Qual é o tipo de contrato?',
    ('Mês a Mês', 'Um Ano', 'Dois Anos')
)

# Definir a variável apropriada com base na seleção do usuário
if tipo_contrato == 'Mês a Mês':
    Conta_Contrato_MesAMes = 1
elif tipo_contrato == 'Um Ano':
    Conta_Contrato_UmAno = 1
elif tipo_contrato == 'Dois Anos':
    Conta_Contrato_DoisAnos = 1

# Para a forma de pagamento e cobranças na conta
Conta_FormaPagamento_ChequeEletronico = st.radio('A forma de pagamento é via Cheque Eletrônico?', ('Sim', 'Não'))
# Convertendo a resposta em binário
Conta_FormaPagamento_ChequeEletronico = 1 if Conta_FormaPagamento_ChequeEletronico == 'Sim' else 0

CobrancasConta_0_500 = st.radio('As cobranças estão abaixo de 500?', ('Sim', 'Não'))
# Convertendo a resposta em binário
CobrancasConta_0_500 = 1 if CobrancasConta_0_500 == 'Sim' else 0

# Continue para todos os outros recursos...

# Botão para fazer previsões
if st.button('Fazer Previsão'):

    # Criar um array com os valores dos recursos
    features_array = np.array([internet_seguranca_online, internet_suporte_tecnico, permanencia_0_5, permanencia_61_70,
                               permanencia_71_80, Conta_Contrato_MesAMes, Conta_Contrato_UmAno, Conta_Contrato_DoisAnos, 
                               Conta_FormaPagamento_ChequeEletronico, CobrancasConta_0_500])  # Adicione todos os recursos
    
    features_array = features_array.reshape(1, -1)
    
    # Fazer a previsão
    prediction = model.predict(features_array)
    
    # Exibir o resultado
    if prediction[0] == 1:
        st.success('Previsto: Classe 1')
    else:
        st.success('Previsto: Classe 0')
