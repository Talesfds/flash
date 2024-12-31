import streamlit as st
import pandas as pd
from fractions import Fraction

# Função para calcular o valor baseado na Abertura
def calcular_valor_abertura(abertura):
    if abertura == 16:
        return 1
    elif abertura == 11:
        return 2
    elif abertura == 8:
        return 3
    elif abertura == 5.6:
        return 4
    elif abertura == 4.0:
        return 5
    elif abertura == 2.8:
        return 6
    elif abertura == 2.0:
        return 7
    elif abertura == 1.4:
        return 8
    elif abertura == 1.0:
        return -9
    elif abertura == 22:  # Nova opção
        return 0
    else:
        return "Valor inválido para abertura"

# Função para calcular o valor baseado no ISO
def calcular_valor_iso(iso):
    if iso == 200:
        return 1
    elif iso == 400:
        return 2
    elif iso == 800:
        return 3
    elif iso == 1600:
        return 4
    elif iso == 3200:
        return 5
    elif iso == 100:  # Nova opção
        return 0
    else:
        return "Valor inválido para ISO"

# Função para calcular o valor baseado na Distância com as novas regras
def calcular_valor_distancia(distancia):
    if distancia == 0.5:
        return 2
    elif distancia == 1.5:
        return -1
    elif distancia == 2.0:
        return -2
    elif distancia == 3.0:
        return -3
    elif distancia == 4.0:
        return -4
    elif distancia == 5.0:
        return -5
    elif distancia == 1:  # Nova opção
        return 0
    else:
        return "Valor inválido para distância"

# Função para calcular o valor baseado na Potência com as novas regras
def calcular_valor_potencia(potencia):
    if potencia == Fraction(1, 1):
        return 0
    elif potencia == Fraction(1, 2):
        return -1
    elif potencia == Fraction(1, 4):
        return -2
    elif potencia == Fraction(1, 8):
        return -3
    elif potencia == Fraction(1, 16):
        return -4
    elif potencia == Fraction(1, 32):
        return -5
    elif potencia == Fraction(1, 64):
        return -6
    elif potencia == Fraction(1, 128):
        return -7
    elif potencia == Fraction(1, 256):
        return -8
    else:
        return "Valor inválido para potência"

# Função para calcular o valor baseado no Modificador
def calcular_valor_modificador(modificador):
    if modificador == 'Flash Direto':
        return 0
    elif modificador == 'Softbox':
        return -2
    elif modificador == 'Softbox + Grid':
        return -3
    else:
        return "Valor inválido para modificador"

# Função para formatar o valor da coluna EV com o sinal "+" para positivos
def formatar_valor_ev(valor):
    if isinstance(valor, (int, float)):
        return f"+{valor}" if valor > 0 else f"{valor}"
    return valor

# Título da página
st.title('Fotometria do Flash')

# Seleção de valores para Abertura, ISO, Distância, Potência e Modificador
abertura = st.selectbox('Abertura', [22,16, 11, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0], index=0, key="abertura")
iso = st.selectbox('ISO', [100,200, 400, 800, 1600, 3200], index=0, key="iso")
distancia = st.selectbox('Distância', [1,0.5, 1.5, 2.0, 3.0, 4.0,5.0], index=0, key="distancia")

# Convertendo os valores da potência para frações e exibição no selectbox
potencia_opcoes = [Fraction(1, 1), Fraction(1, 2), Fraction(1, 4), Fraction(1, 8), 
                   Fraction(1, 16), Fraction(1, 32), Fraction(1, 64), Fraction(1, 128), Fraction(1, 256)]
potencia = st.selectbox('Potência', potencia_opcoes, index=0, format_func=lambda x: str(x), key="potencia")

# Seleção do Modificador
modificador = st.selectbox('Modificador', ['Flash Direto', 'Softbox', 'Softbox + Grid'], index=0, key="modificador")

# Calculando os valores finais
valor_abertura = calcular_valor_abertura(abertura)
valor_iso = calcular_valor_iso(iso)
valor_distancia = calcular_valor_distancia(distancia)
valor_potencia = calcular_valor_potencia(potencia)
valor_modificador = calcular_valor_modificador(modificador)

# Formatando os valores com o "+" para positivos
valor_abertura = formatar_valor_ev(valor_abertura)
valor_iso = formatar_valor_ev(valor_iso)
valor_distancia = formatar_valor_ev(valor_distancia)
valor_potencia = formatar_valor_ev(valor_potencia)
valor_modificador = formatar_valor_ev(valor_modificador)

# Criando um dataframe para exibir como tabela
data = {
    'Parâmetro': ['Abertura', 'ISO', 'Distância', 'Potência', 'Modificador'],
    'Valor Selecionado': [abertura, iso, distancia, str(potencia), modificador],
    'EV (valor)': [valor_abertura, valor_iso, valor_distancia, valor_potencia, valor_modificador]
}

df = pd.DataFrame(data)

# Somando a coluna "EV (valor)" (convertendo todos os valores para int, para soma)
df['EV (valor)'] = pd.to_numeric(df['EV (valor)'], errors='coerce')
soma_ev = df['EV (valor)'].sum()

# Adicionando a linha de soma ao final do DataFrame com "EV Final"
soma_data = pd.DataFrame([['EV Final', '', soma_ev]], columns=df.columns)
df = pd.concat([df, soma_data], ignore_index=True)

# Centralizando os valores das colunas e destacando a linha de soma
df = df.style.set_properties(subset=['Valor Selecionado', 'EV (valor)'], **{'text-align': 'center'})



# Exibindo a tabela
st.table(df)
