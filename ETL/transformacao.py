import pandas as pd

def transformar_dados(df_estoque, df_produtos):
    if df_estoque.empty or df_produtos.empty:
        print("❌ Erro: Um dos DataFrames está vazio!")
        return pd.DataFrame()  # Retorna um DataFrame vazio

    # Tentar o merge 
    df_estoque_produtos = df_estoque.merge(
        df_produtos, 
        left_on="produto_id", 
        right_on="id", 
        how="left"
    )
    
    # KPI para exibir todos os produtos
    df_total_estoque = df_estoque['quantidade'].sum()

    

    return df_estoque_produtos, df_total_estoque