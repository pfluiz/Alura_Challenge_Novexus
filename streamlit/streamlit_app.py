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
from joblib import load
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Função para carregar dados do CSV
@st.cache  # Substitui o st.cache depreciado
def load_data():
    data = pd.read_csv('df_balanceado.csv')  # Removendo o caminho absoluto
    return data


# Carregar os dados
data = load_data()

# ... importações e outras definições

st.title("Previsão de Churn para Novexus")
st.markdown("### Sobre esta ferramenta")
st.markdown("Esta ferramenta prevê o risco de um cliente abandonar (Churn) a Novexus. Preencha as informações abaixo e clique em 'Prever Churn'.")
# Opções para inserção de dados
tenure_0_5 = st.checkbox('Tempo de Permanência 0-5 meses')
account_month_to_month = st.checkbox('Contrato Mês-a-Mês')
account_two_year = st.checkbox('Contrato de Dois Anos')
account_charges_0_500 = st.checkbox('Cobranças 0-500')

# Montar o DataFrame com base nas entradas
input_data = {
    'tenure_0-5': [int(tenure_0_5)],
    'account_Contract_MONTH-TO-MONTH': [int(account_month_to_month)],
    'account_Contract_TWO YEAR': [int(account_two_year)],
    'account_charges_0-500': [int(account_charges_0_500)]
}

input_df = pd.DataFrame(input_data)

if st.button("Prever Churn"):
    # Carregar o modelo previamente treinado
    loaded_model = load(r'C:\Users\paulo\OneDrive\Área de Trabalho\best_lr_model.pkl')
    
    # Fazer a previsão
    prediction = loaded_model.predict(input_df)
    
    # Exibir resultado
    if prediction[0] == 1:
        st.write("O cliente ESTÁ em risco de Churn!")
    else:
        st.write("O cliente NÃO está em risco de Churn.")

st.markdown("### Versão do Modelo")
st.markdown("Modelo de Regressão Logística otimizado para Recall")


