import pandas as pd
from sqlalchemy import create_engine

def Extrair_dados():
    server = r"PEDRO-H\SQLEXPRESS"  # Altere se necessário
    database = "estoque_db"

    # Criando a engine do SQLAlchemy
    engine = create_engine(f"mssql+pyodbc://@{server}/{database}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server") #?trusted_connection=yes Autenticaçao do Windows no SQL server

    try:
        # Criando conexão
        conn = engine.connect()
        print("✅ Conexão bem-sucedida!")

        # Extração dos dados
        df_estoque = pd.read_sql("SELECT * FROM Estoque", conn)
        df_produtos = pd.read_sql("SELECT * FROM Produtos", conn)

        # Fechando a conexão
        conn.close()

        return df_estoque, df_produtos

    except Exception as e:
        print(f"❌ Erro ao conectar ao SQL Server: {e}")
        return None, None  # Retorna DataFrames vazios em caso de erro

# Executando a função de extração
df_estoque, df_produtos = Extrair_dados()
