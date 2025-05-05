import pandas as pd
from sqlalchemy import create_engine

def Extrair_dados():
    server = r"PEDRO-H\SQLEXPRESS"
    database = "estoque_db"
    engine = create_engine(f"mssql+pyodbc://@{server}/{database}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server")

    # Esquema padrão para DataFrames vazios
    empty_df_schema = {
        'produtos': pd.DataFrame(columns=['id', 'nome', 'categoria', 'preco']),
        'estoque': pd.DataFrame(columns=['id', 'produto_id', 'quantidade', 'data_atualizacao']),
        'vendas': pd.DataFrame(columns=['id', 'produto_id', 'quantidade_vendida', 'data_venda']),
        'regioes': pd.DataFrame(columns=['id', 'nome', 'descricao']),
        'vendas_regioes': pd.DataFrame(columns=['id', 'venda_id', 'regiao_id'])
    }

    try:
        conn = engine.connect()
        print("✅ Conexão bem-sucedida!")

        # Extração com tratamento explícito
        df_produtos = pd.read_sql("SELECT id, nome, categoria, preco FROM Produtos", conn)
        df_estoque = pd.read_sql("SELECT id, produto_id, quantidade, data_atualizacao FROM Estoque", conn)
        df_vendas = pd.read_sql("SELECT id, produto_id, quantidade_vendida, data_venda FROM Vendas", conn)
        df_regioes = pd.read_sql("SELECT id, nome, descricao FROM Regioes", conn)
        df_vendas_regioes = pd.read_sql("SELECT id, venda_id, regiao_id FROM Vendas_Regioes", conn)

        # Normalização CORRETA das colunas (cada DataFrame separadamente)
        df_produtos.columns = df_produtos.columns.str.strip().str.lower()
        df_estoque.columns = df_estoque.columns.str.strip().str.lower()
        df_vendas.columns = df_vendas.columns.str.strip().str.lower()
        df_regioes.columns = df_regioes.columns.str.strip().str.lower()
        df_vendas_regioes.columns = df_vendas_regioes.columns.str.strip().str.lower()

        # Verificação imediata
        if df_estoque.empty or df_produtos.empty:
            print("⚠️ Aviso: DataFrame vazio detectado na extração")
            
        conn.close()
        return df_produtos, df_estoque, df_vendas, df_regioes, df_vendas_regioes

    except Exception as e:
        print(f"❌ Erro crítico na extração: {str(e)}")
        # Retorna DataFrames vazios com estrutura conhecida
        return (empty_df_schema['produtos'], empty_df_schema['estoque'], 
                empty_df_schema['vendas'], empty_df_schema['regioes'], 
                empty_df_schema['vendas_regioes'])