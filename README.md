## Instalação
Instruções para configurar o ambiente local e rodar o projeto.

```bash
# Clone o repositório
git clone https://github.com/CaioSoares-V8/desafio_conexao_bd.git

# Crie um ambiente virtual
python -m venv venv

# Acesse esse ambiente
venv\Scripts\activate.bat

# Instale as dependências
pip install -r requirements.txt

# Crie o seu banco em SQL Server
# Utilize este modelo de tabela para facilitar a implementação
create table usuarios (
id_usuario int primary key identity(1,1),
nome varchar(50),
cpf char(11),
email varchar(100),
telefone varchar(20),
estado char(2),
capital varchar(50),
bairro varchar(50),
rua varchar(100),
complemento varchar(100)
);

# Configure as variáveis de ambiente do arquivo .env de acordo com as configurações de seu banco SQL Server
SQL_SERVER = # Seu servidor do SQL Server 
SQL_DATABASE = # O nome do banco de dados criado
SQL_USERNAME = # Credenciais de Usuário
SQL_PASSWORD = # Sua senha de acesso

# Execute a aplicação
streamlit run app.py
```