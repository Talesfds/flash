import streamlit as st
import math
from fractions import Fraction



# Função para cálculo baseado no sufixo
def calcular_valor_abertura(abertura):
    if sufixo_flash == "NG22":
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
            return 9
        elif abertura == 22:
            return 0

        else:
            return "Valor inválido para abertura"
    
    elif sufixo_flash == "NG45":
        if abertura == 45:
            return 0
        elif abertura == 32:
            return 1
        elif abertura == 22:
            return 2
        elif abertura == 16:
            return 3
        elif abertura == 11:
            return 4
        elif abertura == 8.0:
            return 5
        elif abertura == 5.6:
            return 6
        elif abertura == 4.0:
            return 7
        elif abertura == 2.8:
            return 8
        elif abertura == 2.0:
            return 9
        elif abertura == 1.4:
            return 10
        elif abertura == 1.0:
            return 11
        else:
            return "Valor inválido para abertura"
    
    elif sufixo_flash == "NG64":
        if abertura == 64:
            return 0
        if abertura == 45:
            return 1
        elif abertura == 32:
            return 2
        elif abertura == 22:
            return 3
        elif abertura == 16:
            return 4
        elif abertura == 11:
            return 5
        elif abertura == 8.0:
            return 6
        elif abertura == 5.6:
            return 7
        elif abertura == 4.0:
            return 8
        elif abertura == 2.8:
            return 9
        elif abertura == 2.0:
            return 10
        elif abertura == 1.4:
            return 11
        elif abertura == 1.0:
            return 12
        else:
            return "Valor inválido para abertura"
    
    elif sufixo_flash == "NG16":
        if abertura == 16:
            return 0
        elif abertura == 11:
            return 1
        elif abertura == 8:
            return 2
        elif abertura == 5.6:
            return 3
        elif abertura == 4.0:
            return 4
        elif abertura == 2.8:
            return 5
        elif abertura == 2.0:
            return 6
        elif abertura == 1.4:
            return 7
        elif abertura == 1.0:
            return 8
        else:
            return "Valor inválido para abertura"

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

def calcular_valor_modificador(modificador):
    if modificador == 'Flash Direto':
        return 0
    elif modificador == 'Softbox Padrão(2 Difusores)':
        return -2   
    elif modificador == 'Softbox com 1 Difusor':
        return -1
    elif modificador == 'Softbox com 2 Difusores + Grid':
        return -3
    elif modificador == 'Softbox com 1 Difusor + Grid':
        return -2
    else:
        return "Valor inválido para modificador"

def calcular_valor_filtro_nd(filtro):
    if filtro == "Sem Filtro":
        return 0
    elif filtro == "ND2":
        return -1
    elif filtro == "ND4":
        return -2
    elif filtro == "ND8":
        return -3
    elif filtro == "ND16":
        return -4
    elif filtro == "ND32":
        return -5
    elif filtro == "ND64":
        return -6
    elif filtro == "ND100":
        return -7
    elif filtro == "ND128":
        return -7
    elif filtro == "ND256":
        return -8
    elif filtro == "ND400":
        return -9
    elif filtro == "ND512":
        return -9
    elif filtro == "ND1000":
        return -10
    else:
        return "Valor inválido para Filtro ND"

# Função para formatar o valor da coluna EV com o sinal "+" para positivos
def formatar_valor_ev(valor):
    if isinstance(valor, (int, float)):
        return f"+{valor}" if valor > 0 else f"{valor}"
    return valor

flash_aberturas = {
    "Younguo YN460 - NG16": [16,11, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0],
    "Younguo YN560 - NG22": [22, 16, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0],
    "Younguo YN600 EX RT - NG22": [22, 16, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0],
    "Younguo YN968 - NG22": [22, 16, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0],
    "Younguo YN200 - NG45": [45, 32, 22, 16, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0],
    "Canon 430EX III - NG22": [22, 16, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0],
    "Canon 600EX II - NG22": [22, 16, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0],
    "Nikon SB700 - NG22": [22, 16, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0],
    "Nikon SB800 - NG22": [22, 16, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0],
    "Nikon SB900 - NG22": [22, 16, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0],
    "Nikon SB910 - NG22": [22, 16, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0],
    "Nikon SB5000 - NG22": [22, 16, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0],
    "Godox TT685 - NG22": [22, 16, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0],
    "Godox V860 - NG22": [22, 16, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0],
    "Godox V1 - NG22": [22, 16,8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0],
    "Godox AD200 - NG45": [45, 32, 22, 16, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0],
    "Godox AD360 - NG45": [45, 32, 22, 16, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0],
    "Godox AD600 - NG64": [64, 45, 32, 22, 16, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0],
    "Menik LD400 - NG45": [45, 32, 22, 16, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0],
    "Godox DP600 - NG64": [64, 45, 32, 22, 16, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0],
    "Godox DE300 - NG45": [45, 32, 22, 16, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0],
    "Godox SK 300II - NG64": [64, 45, 32, 22, 16, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0],
    "Atek 200 Digital Control - NG22": [22, 16, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0],
    "Vivitar 283 - NG22": [22, 16, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0],
    "Profoto A1 - NG22": [22, 16, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0],
    "Westcott FJ400 - NG32": [32, 22, 16, 8, 5.6, 4.0, 2.8, 2.0, 1.4, 1.0]
}


# Código principal
st.title("Fotometria do Flash")

# Painel de controle no sidebar
st.sidebar.markdown("## Configurações")

# Lista para seleção do Flash
flash_options = list(flash_aberturas.keys())
flash_selected = st.sidebar.selectbox("Selecione o Flash", options=flash_options)

# Extrair o sufixo do flash selecionado (exemplo: NG45)
sufixo_flash = flash_selected.split(" - ")[-1]  # Pega tudo após o " - "

# Seleção da Abertura baseada no flash selecionado
aperture_options = flash_aberturas[flash_selected]  # Obtendo as aberturas para o flash selecionado
aperture_selected = st.sidebar.selectbox("Selecione a Abertura", options=aperture_options)


# Seleção do ISO
iso_options = [100,200, 400, 800, 1600, 3200]
iso_selected = st.sidebar.selectbox("Selecione o ISO", options=iso_options)

# Seleção da Distância
distance_options = [1,0.5, 1.5, 2.0, 3.0, 4.0, 5.0]
distance_selected = st.sidebar.selectbox("Selecione a Distância (em metros)", options=distance_options)

# Seleção da Potência
power_options = ["1/1", "1/2", "1/4", "1/8", "1/16", "1/32", "1/64", "1/128", "1/256"]
power_selected = st.sidebar.selectbox("Selecione a Potência", options=power_options)

# Seleção do Modificador
modifier_options = ["Flash Direto", "Softbox Padrão(2 Difusores)", "Softbox com 1 Difusor","Softbox com 2 Difusores + Grid","Softbox com 1 Difusor + Grid" ]
modifier_selected = st.sidebar.selectbox("Selecione o Modificador", options=modifier_options)

# Seleção do Filtro ND
nd_filter_options = [
    "Sem Filtro", "ND2", "ND4", "ND8", "ND16", "ND32", "ND64", "ND100", "ND128", "ND256", "ND400", "ND512", "ND1000"
]
nd_filter_selected = st.sidebar.selectbox("Selecione o Filtro ND", options=nd_filter_options)

# Exibição da tabela com os valores dentro de um retângulo
st.markdown('<div class="rectangle"><h3>Valores Selecionados</h3><div class="table">', unsafe_allow_html=True)

# Exibindo as configurações dentro do retângulo
st.markdown(f"""
<div style="display: flex; flex-direction: column; padding: 10px; border: 2px solid #ddd; border-radius: 10px; background-color: #f9f9f9;">
    <div><strong>Flash:</strong> {flash_selected}</div>
    <div><strong>Abertura:</strong> {aperture_selected}</div>
    <div><strong>ISO:</strong> {iso_selected}</div>
    <div><strong>Distância:</strong> {distance_selected} m</div>
    <div><strong>Potência:</strong> {power_selected}</div>
    <div><strong>Modificador:</strong> {modifier_selected}</div>
    <div><strong>Filtro ND:</strong> {nd_filter_selected}</div>
</div>
""", unsafe_allow_html=True)


st.markdown('</div></div>', unsafe_allow_html=True)  # Fecha o retângulo

# Exibição de informações adicionais na linha abaixo
st.markdown("### Calculadora de EV")

col2, col3, col4, col5, col6, col7 = st.columns(6)  # Adicionando a coluna para o Filtro ND

with col2:
    st.markdown("<div style='text-align: center;border: 2px solid #ddd; border-radius: 10px; background-color: #f9f9f9'>Abertura:</div>", unsafe_allow_html=True)
    valor_abertura = calcular_valor_abertura(aperture_selected)
    st.markdown(f"""
    <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
        <span style="color: blue; font-size: 30px;">{formatar_valor_ev(valor_abertura)}</span>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("<div style='text-align: center;border: 2px solid #ddd; border-radius: 10px; background-color: #f9f9f9'>ISO:</div>", unsafe_allow_html=True)
    valor_iso = calcular_valor_iso(iso_selected)
    st.markdown(f"""
    <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
        <span style="color: blue; font-size: 30px;">{formatar_valor_ev(valor_iso)}</span>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("<div style='text-align: center;border: 2px solid #ddd; border-radius: 10px; background-color: #f9f9f9'>Distância:</div>", unsafe_allow_html=True)
    valor_distancia = calcular_valor_distancia(distance_selected)
    st.markdown(f"""
    <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
        <span style="color: blue; font-size: 30px;">{formatar_valor_ev(valor_distancia)}</span>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("<div style='text-align: center;border: 2px solid #ddd; border-radius: 10px; background-color: #f9f9f9'>Potência:</div>", unsafe_allow_html=True)
    potencia_value = Fraction(power_selected)
    valor_potencia = calcular_valor_potencia(potencia_value)
    st.markdown(f"""
    <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
        <span style="color: blue; font-size: 30px;">{formatar_valor_ev(valor_potencia)}</span>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("<div style='text-align: center;border: 2px solid #ddd; border-radius: 10px; background-color: #f9f9f9'>Modificador:</div>", unsafe_allow_html=True)
    valor_modificador = calcular_valor_modificador(modifier_selected)
    st.markdown(f"""
    <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
        <span style="color: blue; font-size: 30px;">{formatar_valor_ev(valor_modificador)}</span>
    </div>
    """, unsafe_allow_html=True)

with col7:
    st.markdown("<div style='text-align: center;border: 2px solid #ddd; border-radius: 10px; background-color: #f9f9f9'>Filtro ND:</div>", unsafe_allow_html=True)
    valor_filtro_nd = calcular_valor_filtro_nd(nd_filter_selected)
    st.markdown(f"""
    <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
        <span style="color: blue; font-size: 30px;">{formatar_valor_ev(valor_filtro_nd)}</span>
    </div>
    """, unsafe_allow_html=True)


# Cálculo da soma final
soma_final = (valor_abertura + valor_iso + valor_distancia + valor_potencia + valor_modificador + valor_filtro_nd)

