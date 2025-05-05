import pyodbc

server = ""  # Nome do servidor
database = ""  # Nome do banco de dados (alterar conforme necessário)
trusted_connection = ""  # Usa autenticação do Windows

conn_str = (
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=' + server + ';'
    r'DATABASE=' + database + ';'
    r'Trusted_Connection=' + trusted_connection + ';'
)

try:
    conn = pyodbc.connect(conn_str)
    print("✅ Conexão com SQL Server bem-sucedida!")
    conn.close()
except Exception as e:
    print(f"❌ Erro na conexão: {e}")