import streamlit as st
import duckdb
import os
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Preditor de Sucesso", layout="wide")

# Conexão com o banco
caminho_da_pasta = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(caminho_da_pasta, 'empresa_vendas.db')
con = duckdb.connect(db_path)

st.title("🚀 Painel Executivo - Preditor de Sucesso")
st.markdown("---")

# --- BLOCO 1: KPI'S ---
col1, col2, col3 = st.columns(3)
faturamento = con.execute("SELECT SUM(valor) FROM trusted_vendas").fetchone()[0]
lucro_total = con.execute("SELECT SUM(lucro) FROM trusted_vendas").fetchone()[0]
total_pedidos = con.execute("SELECT COUNT(*) FROM trusted_vendas").fetchone()[0]

col1.metric("Faturamento Total", f"R$ {faturamento:,.2f}")
col2.metric("Lucro Total", f"R$ {lucro_total:,.2f}")
col3.metric("Qtd. Pedidos", f"{total_pedidos}")

# --- BLOCO 2: GRÁFICOS ---
st.markdown("### Top 5 Clientes por Lucro")
top_clientes = con.execute("""
    SELECT cliente, SUM(lucro) as lucro_total 
    FROM trusted_vendas 
    GROUP BY cliente 
    ORDER BY lucro_total DESC 
    LIMIT 5
""").df()

# Criando o gráfico com Matplotlib
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(top_clientes['cliente'], top_clientes['lucro_total'], color='skyblue')
ax.set_ylabel('Lucro em R$')
ax.set_title('Os Clientes que mais geram valor')

st.pyplot(fig)

# --- BLOCO 3: TABELA DE DADOS ---
st.markdown("### Dados Brutos (Camada Trusted)")
df_view = con.execute("SELECT * FROM trusted_vendas LIMIT 100").df()
st.dataframe(df_view)