import pandas as pd
import traceback

def transformar_dados(df_estoque, df_produtos, df_vendas, df_regioes, df_vendas_regioes):
    # Esquema para resultados vazios
    empty_results = {
        "estoque_baixo": pd.DataFrame(),
        "estoque_total": pd.DataFrame(),
        "regioes": pd.DataFrame()
    }
    
    try:
        # Verificação robusta de colunas
        def check_columns(df, df_name, required_cols):
            if df.empty:
                raise ValueError(f"DataFrame {df_name} está vazio")
                
            missing = [col for col in required_cols if col not in df.columns]
            if missing:
                available = df.columns.tolist()
                raise ValueError(
                    f"Coluna(s) faltante(s) em {df_name}: {missing}\n"
                    f"Colunas disponíveis: {available}"
                )

        # Verifica todas as colunas necessárias
        check_columns(df_estoque, 'df_estoque', ['produto_id', 'quantidade'])
        check_columns(df_produtos, 'df_produtos', ['id'])
        check_columns(df_vendas, 'df_vendas', ['id', 'produto_id', 'quantidade_vendida'])
        check_columns(df_vendas_regioes, 'df_vendas_regioes', ['venda_id', 'regiao_id'])
        check_columns(df_regioes, 'df_regioes', ['id', 'nome'])

        # Merge seguro com tratamento de erros
        df_estoque_produtos = pd.merge(
            df_estoque,
            df_produtos,
            left_on="produto_id",
            right_on="id",
            how="left",
            suffixes=('_estoque', '_produto'),
            validate="many_to_one"
        )
        
        # Filtro de estoque baixo
        df_estoque_baixo = df_estoque_produtos[df_estoque_produtos['quantidade'] < 50]

        # Consolidação de regiões com verificação
        df_vendas_com_regioes = pd.merge(
            df_vendas,
            df_vendas_regioes,
            left_on="id",
            right_on="venda_id",
            how="left"
        ).merge(
            df_regioes,
            left_on="regiao_id",
            right_on="id",
            how="left"
        )
        
        # Agregação por região
        df_regioes_completo = df_vendas_com_regioes.groupby(
            ['regiao_id', 'nome', 'descricao']
        ).agg(
            total_vendas=('quantidade_vendida', 'sum')
        ).reset_index().rename(columns={'nome': 'regiao_nome'})

        return {
            "estoque_baixo": df_estoque_baixo,
            "estoque_total": df_estoque_produtos,
            "regioes": df_regioes_completo
        }

    except Exception as e:
        print(f"\n❌ ERRO NA TRANSFORMAÇÃO:")
        traceback.print_exc()
        print("\n🔍 Debug - DataFrames recebidos:")
        print("df_estoque cols:", df_estoque.columns.tolist() if not df_estoque.empty else "VAZIO")
        print("df_produtos cols:", df_produtos.columns.tolist() if not df_produtos.empty else "VAZIO")
        return empty_results