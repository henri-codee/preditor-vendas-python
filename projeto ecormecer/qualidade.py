import duckdb
import os

# 1. Localiza a pasta onde o script está
caminho_da_pasta = os.path.dirname(os.path.abspath(__file__))
caminho_do_banco = os.path.join(caminho_da_pasta, 'empresa_vendas.db')

print(f"--- [AUDITORIA DE QUALIDADE] ---")
print(f"Conectando ao banco em: {caminho_do_banco}")

# Verifica se o arquivo do banco realmente existe antes de tentar abrir
if not os.path.exists(caminho_do_banco):
    print(f"[ERRO] O arquivo 'empresa_vendas.db' não foi encontrado!")
    print("Certifique-se de que você rodou o 'engenharia.py' com sucesso primeiro.")
else:
    con = duckdb.connect(caminho_do_banco)

    try:
        # 1. Verifica se há valores nulos
        # Usamos COUNT(*) - COUNT(coluna) para saber quantos nulos existem
        nulos = con.execute("""
            SELECT 
                (SELECT COUNT(*) FROM trusted_vendas) - COUNT(id_pedido) as nulos_id,
                (SELECT COUNT(*) FROM trusted_vendas) - COUNT(cliente) as nulos_cliente,
                (SELECT COUNT(*) FROM trusted_vendas) - COUNT(valor) as nulos_valor
            FROM trusted_vendas
        """).df()

        # 2. Resumo dos dados
        total_linhas = con.execute("SELECT COUNT(*) FROM trusted_vendas").fetchone()[0]

        print(f"Total de registros no banco: {total_linhas}")
        print(f"Relatório de campos vazios (Nulos):\n{nulos}")

        if nulos.values.sum() == 0:
            print("\n✅ STATUS: DADOS 100% LIMPOS E CONFIÁVEIS!")
        else:
            print("\n⚠️ STATUS: Existem valores nulos. Verifique a fonte.")

    except Exception as e:
        print(f"[ERRO AO ACESSAR TABELA]: {e}")
        print("Dica: Rode o engenharia.py novamente para garantir que a tabela 'trusted_vendas' foi criada.")