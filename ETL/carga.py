import os
import pandas as pd

def salvar_csv(resultados):
    try:
        caminho_pasta = os.path.abspath("G:\\Meu Drive\\monitoramento_estoque")
        caminho_arquivo_total = os.path.join(caminho_pasta, "estoque_total.csv")
        caminho_arquivo_baixo = os.path.join(caminho_pasta, "estoque_baixo.csv")
        caminho_regioes = os.path.join(caminho_pasta, "regioes.csv")
       

        if not os.path.exists(caminho_pasta):
            os.makedirs(caminho_pasta)

        # Salva estoque baixo (produtos filtrados)
        resultados["estoque_baixo"].to_csv(caminho_arquivo_baixo, index=False)
        print(f"✅ Estoque baixo salvo em: {caminho_arquivo_baixo}")

        # Salva estoque total (todos os produtos)
        resultados["estoque_total"].to_csv(caminho_arquivo_total, index=False)
        print(f"✅ Estoque total  salvo em: {caminho_arquivo_total}")
        
        # Salva regiões (Vendas por região)
        resultados["regioes"].to_csv(caminho_regioes, index=False, encoding='utf-8-sig')
        print(f"✅ Regiões salvas em: {caminho_regioes}")

        return resultados["estoque_baixo"]

    except Exception as e:
        print(f"❌ Erro ao salvar os arquivos: {e}")
        return None