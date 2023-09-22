import streamlit as st
import pandas as pd
from joblib import load

# Função para carregar dados do CSV
@st.cache_data  # Substitui o st.cache depreciado
def load_data():
    data = pd.read_csv(r'C:\Users\paulo\OneDrive\Área de Trabalho\df_balanceado.csv')  # Usando r para string raw
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


