from extracao import Extrair_dados
from transformacao import transformar_dados
from carga import salvar_csv

df_estoque, df_produtos = Extrair_dados()
df_estoque_baixo = transformar_dados(df_estoque, df_produtos)
salvar_csv(df_estoque_baixo)

print("✅ ETL finalizado com sucesso!")