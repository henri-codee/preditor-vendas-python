import duckdb
import os

# Localizando o banco
caminho_da_pasta = os.path.dirname(os.path.abspath(__file__))
caminho_do_banco = os.path.join(caminho_da_pasta, 'empresa_vendas.db')

con = duckdb.connect(caminho_do_banco)

print("--- RELATORIO EXECUTIVO DE VENDAS ---")

# 1. FATURAMENTO TOTAL
faturamento = con.execute("SELECT SUM(valor) FROM trusted_vendas").fetchone()[0]
print(f"Faturamento Total da Empresa: R$ {faturamento:,.2f}")

# 2. TOP 5 CLIENTES POR LUCRO
print("\n--- TOP 5 CLIENTES MAIS LUCRATIVOS ---")
top_clientes = con.execute("""
    SELECT cliente, SUM(lucro) as lucro_total 
    FROM trusted_vendas 
    GROUP BY cliente 
    ORDER BY lucro_total DESC 
    LIMIT 5
""").df()
print(top_clientes)

# 3. RANKING DE VENDAS POR REGIAO (Se tiver essa coluna na sua trusted)
# Como no seu script de engenharia reduzimos colunas, vamos focar no que temos:
print("\n--- PERFORMANCE POR PEDIDO (TOP 3) ---")
top_pedidos = con.execute("""
    SELECT id_pedido, cliente, valor 
    FROM trusted_vendas 
    ORDER BY valor DESC 
    LIMIT 3
""").df()
print(top_pedidos)

print("\nRelatorio finalizado com sucesso.")