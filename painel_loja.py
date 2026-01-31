import streamlit as st

st.set_page_config(page_title="Painel +DryWall", layout="wide")
st.title("📊 Painel de Controle +DryWall")

st.info("Clique nos botões abaixo para abrir as planilhas ou o sistema externo. Se já estiver aberto, será reutilizado.")

# Dicionário de links: apenas adicionar novos aqui
links = {
    "📋 Controle de Vendas": [
        "https://docs.google.com/spreadsheets/d/1srsT8tbqhVUlG9u1Z2ZVxrAQxAuHWhRlucpyMeY76MI/edit?gid=1353649574#gid=1353649574",
        "controle_vendas"
    ],
    "🚨 Controle de Aberto": [
        "https://docs.google.com/spreadsheets/d/1M1gZvSCAo1rx8MhbtI8LPDFkmjcUdf4C7StWYEirCUI/edit?gid=1709197134#gid=1709197134",
        "controle_aberto"
    ],
    "📦 Controle de Estoque": [
        "https://docs.google.com/spreadsheets/d/1vsebwQHB9MtQ4hKPsywxY8VwI8i1MYSouAu4vN9O97k/edit?gid=1637020768#gid=1637020768",
        "controle_estoque"
    ],
    "🌐 Emitir NF-e": [
        "https://gfaz05.sistemagestor.com/wwtarqtab.aspx",
        "emitir_nfe"
    ],
    "💱 Controle de Haver": [
        "https://docs.google.com/spreadsheets/d/1n6S7JHhzSVkZYERocQjRtwjgmXWZh9rI0-o1WwfVbDU/edit?gid=0#gid=0",
        "controle_haver"
    ],
    "🧰 Banco de Dados": [
        "https://docs.google.com/spreadsheets/d/11ou24KaRuDJ6SQenK43tRRN8GylsKXee7woh08--0VY/edit?gid=1345820163#gid=1345820163",
        "banco_dados"
    ],
    "📑 Financeiro": [
        "https://docs.google.com/spreadsheets/d/1eDxpYBtJZhzG-AE-pdgIaYInegHESM74_pdZOadGmmk/edit?usp=sharing",
        "financeiro"
    ],
    "🗃️ Cadastro de Produtos": [
        "https://docs.google.com/spreadsheets/d/1HP2eohBCO_LXnz3GmZ5Zhr2uFtMpxRKtL6CEDeEqAbA/edit?usp=sharing",
        "CadastroProdutos"
    ],
    "🚚 Calculo de Frete": [
        "https://docs.google.com/spreadsheets/d/1AQcLr-cAA6YD1jbJXyv9AGs_UICkyyD9d0m4v2DticI/edit?usp=sharing",
        "calculofretes"
    ],
    "♻️ Pedido de Entrada": [
        "https://docs.google.com/spreadsheets/d/1H7k_FB736y4aHhIfEEMlRF8hvAXF9tBVbshINdtWbkI/edit?usp=drive_link",
        "pedidoEntrada"
    ],
    "📠Vender": [
        "https://docs.google.com/spreadsheets/d/1ykz9y04WJgL_UBxIZt3D8NTZ8Pk7oErWTgL29NDmb4w/edit?usp=drive_link",
        "pedidoEntrada"
    ],
    "1️⃣ Lançar Frete": [
        "https://docs.google.com/forms/d/e/1FAIpQLSeOBweel9kY14p_ge8y5cJERnBdjOGQcj0C6eMKxxkgdu0Pkw/viewform",
        "Lançar Frete"
    ],
    "2️⃣ Lançar Despesas": [
        "https://docs.google.com/forms/d/e/1FAIpQLSfmY8ryx46rdxWh9r52LC1sJJ3Sys0VBHIz03gUQMA1K7p_BA/viewform",
        "Lançardespesas"
    ],
    "3️⃣ Lançar Ajuste Estoque": [
        "https://docs.google.com/forms/d/e/1FAIpQLScAxV26SeqvDnruPkFDd0KAxZtHbYBaUWlL3hKF1W83Vtx1HQ/viewform",
        "Lançarestoque"
    ]




}

# HTML e CSS responsivo
html_content = """
<style>
.custom-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.8rem 1rem;
    background-color: rgb(19, 23, 32);
    color: white;
    border-radius: 0.5rem;
    font-weight: 500;
    font-size: 16px;
    border: none;
    width: 100%;
    cursor: pointer;
    min-height: 60px;
}
.custom-btn:hover {
    background-color: rgb(42, 48, 60);
}
.container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 12px;
}
</style>
<div class="container">
"""

for nome, (url, win_name) in links.items():
    html_content += f"""
    <button class="custom-btn" onclick="window.open('{url}', '{win_name}', 'width=1200,height=800,left=200,top=100');">
        {nome}
    </button>
    """

html_content += "</div>"

# Altura adaptável: calculada pelo número de linhas necessárias
st.components.v1.html(html_content, height=(len(links)//3 + 1) * 80)
