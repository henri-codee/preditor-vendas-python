import duckdb
import os
import pandas as pd

# 1. CONEXÃO
caminho_da_pasta = os.path.dirname(os.path.abspath(__file__))
caminho_do_banco = os.path.join(caminho_da_pasta, 'empresa_vendas.db')
con = duckdb.connect(caminho_do_banco)

print("--- [INTELIGÊNCIA PREDITIVA] ---")

# 2. EXTRAÇÃO DE SÉRIE TEMPORAL
# Vamos agrupar as vendas por data para ver a evolução
dados_tempo = con.execute("""
    SELECT data, SUM(valor) as total_dia 
    FROM trusted_vendas 
    GROUP BY data 
    ORDER BY data
""").df()

# 3. CÁLCULOS ESTATÍSTICOS
faturamento_atual = dados_tempo['total_dia'].sum()
media_venda_diaria = dados_tempo['total_dia'].mean()
meta = 600000000.00  # Meta de 600 Milhões
falta_para_meta = meta - faturamento_atual
dias_estimados = falta_para_meta / media_venda_diaria

print(f"Faturamento Atual: R$ {faturamento_atual:,.2f}")
print(f"Média de Vendas por Dia: R$ {media_venda_diaria:,.2f}")
print(f"\n--- PROJEÇÃO DE SUCESSO ---")
print(f"Para atingir a meta de R$ 600 Milhões, faltam: R$ {falta_para_meta:,.2f}")
print(f"No ritmo atual, a meta será atingida em aproximadamente: {dias_estimados:.0f} dias.")

# 4. INSIGHT DE CIÊNCIA DE DADOS
# Verificando se as vendas estão subindo ou descendo (Tendência)
primeira_metade = dados_tempo['total_dia'].head(len(dados_tempo)//2).mean()
segunda_metade = dados_tempo['total_dia'].tail(len(dados_tempo)//2).mean()

if segunda_metade > primeira_metade:
    print("Tendência: CRESCENTE. O faturamento está acelerando!")
else:
    print("Tendência: QUEDA. É necessário aplicar novas estratégias de marketing.")