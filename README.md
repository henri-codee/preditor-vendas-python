# 🚀 Preditor de Sucesso de Vendas - E-commerce

Este projeto é um ecossistema completo de Inteligência de Dados. Ele simula o fluxo real de uma empresa, desde a recepção de dados brutos até a criação de dashboards interativos e análises preditivas de faturamento.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.12+
- **Banco de Dados:** DuckDB (Alta performance para análise)
- **Dashboard:** Streamlit
- **Visualização de Dados:** Matplotlib
- **Manipulação de Dados:** Pandas

## 🏗️ Estrutura do Projeto (Pipeline de Dados)

O projeto está dividido em camadas para garantir a organização e qualidade dos dados:

1.  **Engenharia (`engenharia.py`):** Realiza a ingestão do arquivo `data.csv`, cria o banco de dados relacional e estrutura a camada `trusted` (dados limpos e prontos para uso).
2.  **Qualidade (`qualidade.py`):** Realiza uma auditoria automatizada para verificar valores nulos, duplicados e anomalias financeiras.
3.  **Análise (`analista.py`):** Extrai KPIs estratégicos como faturamento total, ticket médio e os clientes mais lucrativos.
4.  **Preditor (`preditor.py`):** Utiliza lógica de série temporal para projetar quando a empresa atingirá metas de faturamento e identifica tendências de crescimento ou queda.
5.  **Dashboard (`dashboard.py`):** Interface visual interativa para exploração dos dados em tempo real.

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/henri-codee/preditor-vendas-python.git](https://github.com/henri-codee/preditor-vendas-python.git)
   cd preditor-vendas-python
