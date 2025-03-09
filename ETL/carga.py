import os
import pandas as pd

def salvar_csv(resultado_transformacao):
    try:
        # Define o caminho absoluto usando os.path
        caminho_pasta = os.path.abspath("G:/Meu Drive/Monitoramento_Estoque")
        caminho_arquivo = os.path.join(caminho_pasta, "estoque_total.csv")

        # Verifica se o resultado é uma tupla (DataFrame, total_estoque)
        if isinstance(resultado_transformacao, tuple):
            df_completo, total_estoque = resultado_transformacao

            # Salva o DataFrame completo como CSV
            df_completo.to_csv(caminho_arquivo, index=False)
            print(f"✅ Dados salvos em: {caminho_arquivo}")

            # Retorna o total de estoque para uso posterior, se necessário
            return total_estoque
        else:
            print("❌ Erro: O resultado da transformação não é uma tupla válida.")
            return None

    except Exception as e:
        print(f"❌ Erro ao salvar o arquivo: {e}")
        return None