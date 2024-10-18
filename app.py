import streamlit as st
import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()

server = os.getenv('SQL_SERVER')
database = os.getenv('SQL_DATABASE')
username = os.getenv('SQL_USERNAME')
password = os.getenv('SQL_PASSWORD')

conexao = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
cursor = conexao.cursor()

st.title('Formulario')

ufs_brasil = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 
              'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 
              'RR', 'SC', 'SP', 'SE', 'TO']

with st.form(key='formulario_cadastro'):
    nome = st.text_input('Nome', placeholder='Digite seu nome completo')
    cpf = st.text_input('CPF', placeholder='Somente os números')
    email = st.text_input('E-mail', placeholder='Ex. seunome@email.com')
    telefone = st.text_input('Telefone', placeholder='Somente os números')
    estado = st.selectbox('Estado (UF)', ufs_brasil)
    capital = st.text_input('Capital', placeholder='Ex. São Paulo')
    bairro = st.text_input('Bairro', placeholder='Ex. Capão Redondo')
    rua = st.text_input('Rua', placeholder='Ex. Rua das flores, 129')
    complemento = st.text_input('Complemento', placeholder='Opcional')
    submit_button = st.form_submit_button(label='Enviar')

botao_exibir = st.button('Exibir usuários')

def enviar_dados():
    cursor.execute(f'''
                   insert into usuarios (nome, cpf, email, telefone, estado, capital, bairro, rua, complemento) values
                   ('{nome}', '{cpf}', '{email}', '{telefone}', '{estado}', '{capital}', '{bairro}', '{rua}', '{complemento}');
                   ''')
    conexao.commit()

def exibir_usuarios():
    cursor.execute('select * from usuarios;')
    resultados = cursor.fetchall()
    for item in resultados:
        card_html = f"""
        <div style="border: 1px solid #ddd; border-radius: 10px; padding: 20px; margin-bottom: 10px;">
            <p><b>Nome:</b> {item.nome}</p>
            <p><b>CPF:</b> {item.cpf}</p>
            <p><b>E-mail:</b> {item.email}</p>
            <p><b>Telefone:</b> {item.telefone}</p>
            <p><b>Estado:</b> {item.estado}</p>
            <p><b>Capital:</b> {item.capital}</p>
            <p><b>Bairro:</b> {item.bairro}</p>
            <p><b>Rua:</b> {item.rua}</p>
            <p><b>Complemento:</b> {item.complemento}</p>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)

if botao_exibir:
    exibir_usuarios()

def validar_dados():
    if not nome:
        return 'O campo Nome está vazio'
    elif not cpf:
        return 'O campo CPF está vazio'
    elif len(cpf) < 11:
        return 'Insira um CPF válido'
    elif not email:
        return 'O campo E-mail está vazio'
    elif not '@' in email:
        return 'Insira um E-mail válido'
    elif not telefone:
        return 'O campo Telefone está vazio'
    elif not estado:
        return 'Selecione uma UF válida'
    elif not capital:
        return 'O campo Capital está vazio'
    elif not bairro:
        return 'O campo Bairro está vazio'
    elif not rua:
        return 'O campo Rua está vazio'
    else:
        st.success(f'Dados enviados com sucesso!')
        enviar_dados()

if submit_button:
    resultado = validar_dados()
    
    if resultado:
        st.warning(f"⚠️ {resultado}")




