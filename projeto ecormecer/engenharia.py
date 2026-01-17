import duckdb
import os
import pandas as pd

# 1. LOCALIZAÇÃO
caminho_da_pasta = os.path.dirname(os.path.abspath(__file__))
print(f"--- [DEBUG] Verificando a pasta: {caminho_da_pasta}")

# 2. SCANNER (Vamos ver o que tem na pasta de verdade)
arquivos_na_pasta = os.listdir(caminho_da_pasta)
print(f"--- [DEBUG] Arquivos encontrados: {arquivos_na_pasta}")

# Tenta achar QUALQUER arquivo que termine com .csv
csv_encontrado = [f for f in arquivos_na_pasta if f.lower().endswith('.csv')]

if not csv_encontrado:
    print(f"\n[ERRO CRÍTICO] Não existe NENHUM arquivo .csv dentro de: {caminho_da_pasta}")
    print("Ação: Arraste o arquivo de dados para dentro desta pasta agora!")
else:
    arquivo_alvo = csv_encontrado[0]
    caminho_final = os.path.join(caminho_da_pasta, arquivo_alvo)
    print(f"--- [SUCESSO] Encontrei o arquivo: {arquivo_alvo}")
    
    try:
        # 3. CRIAÇÃO DO BANCO
        con = duckdb.connect(os.path.join(caminho_da_pasta, 'empresa_vendas.db'))
        
        print(f"Carregando {arquivo_alvo} para a STAGE...")
        con.execute(f"CREATE OR REPLACE TABLE stage_vendas AS SELECT * FROM read_csv_auto('{caminho_final}')")
        
        print("Refinando para a camada TRUSTED...")
        con.execute("""
            CREATE OR REPLACE TABLE trusted_vendas AS 
            SELECT 
                "Order ID" AS id_pedido,
                "Order Date" AS data,
                "Customer Name" AS cliente,
                "Sales" AS valor,
                "Profit" AS lucro
            FROM stage_vendas
        """)
        
        print("\n--- MISSION ACCOMPLISHED (MISSÃO CUMPRIDA) ---")
        print(f"Banco 'empresa_vendas.db' gerado com sucesso em: {caminho_da_pasta}")
        print(con.execute("SELECT * FROM trusted_vendas LIMIT 3").df())
        
    except Exception as e:
        print(f"[ERRO NO PROCESSAMENTO]: {e}")