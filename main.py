import pandas as pd
import matplotlib.pyplot as plt

try:
    dados_vendas = pd.read_csv('dados_vendas.csv')
except FileNotFoundError:
    print("O arquivo 'dados_vendas.csv' não foi encontrado.")
else:
    total_vendas = dados_vendas['Quantidade'].sum()
    preco_medio = dados_vendas['Preco Unitario'].mean()
    produtos_mais_vendidos = dados_vendas.groupby('Nome do Produto')['Quantidade'].sum().sort_values(ascending=False).head(3)
    dados_vendas['Data da Venda'] = pd.to_datetime(dados_vendas['Data da Venda'])
    dados_vendas['Mês'] = dados_vendas['Data da Venda'].dt.month
    vendas_por_mes = dados_vendas.groupby('Mês')['Quantidade'].sum()

    plt.figure(figsize=(10, 6))
    plt.plot(vendas_por_mes.index, vendas_por_mes.values, marker='o')
    plt.xlabel('Mês')
    plt.ylabel('Quantidade de Vendas')
    plt.title('Distribuição das Vendas ao Longo do Tempo')
    plt.xticks(range(1, 13))
    plt.grid(True)
    plt.show()
