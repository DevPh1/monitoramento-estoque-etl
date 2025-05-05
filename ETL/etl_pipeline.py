from extracao import Extrair_dados
from transformacao import transformar_dados
from carga import salvar_csv
import sys

def main():
    
    try:
        # 1. Extração
        print("\n[1/3] 🔍 Extraindo dados...")
        df_produtos, df_estoque, df_vendas, df_regioes, df_vendas_regioes = Extrair_dados()
        
        # Verificação crítica
        if df_estoque.empty or df_produtos.empty:
            raise ValueError("Dados essenciais (estoque/produtos) estão vazios")
        
        # 2. Transformação
        print("\n[2/3] 🔄 Transformando dados...")
        resultados = transformar_dados(df_estoque, df_produtos, df_vendas, df_regioes, df_vendas_regioes)
        
        if resultados["estoque_total"].empty:
            raise ValueError("Transformação retornou dados vazios")
        
        # 3. Carga
        print("\n[3/3] 💾 Salvando resultados...")
        salvar_csv(resultados)
        print("✅ Pipeline concluído com sucesso!")
        return 0
        
    except Exception as e:
        print(f"❌ Falha no pipeline {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())