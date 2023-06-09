# -*- coding: utf-8 -*-
"""Exercício3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yeWAtAXrxNmnn7Nlwv8WeJkuhWENj3Pa
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd

# Caminho para o arquivo STORES.csv no Google Drive
file_path = "/content/drive/MyDrive/UNINTER/Python/STORES.csv"

# Ler o arquivo CSV e renomear as colunas
stores_file = pd.read_csv(file_path)
stores_file = stores_file.rename(columns={
    "Items_Available": "Itens Disponíveis",
    "Daily_Customer_Count": "Contagem Diária de Clientes",
    "Store_Sales": "Histórico de Vendas"
})

# Calcular as estatísticas para a coluna Itens Disponíveis
print('\nItens Disponíveis:')
items_min = stores_file["Itens Disponíveis"].min()
print(items_min)
items_max = stores_file["Itens Disponíveis"].max()
print(items_max)
items_mean = stores_file["Itens Disponíveis"].mean()
print(items_mean)
items_std = stores_file["Itens Disponíveis"].std()
print(items_std)

# Calcular as estatísticas para a coluna Contagem Diária de Clientes
print('\nContagem Diária de Clientes:')
customers_min = stores_file["Contagem Diária de Clientes"].min()
print(customers_min)
customers_max = stores_file["Contagem Diária de Clientes"].max()
print(customers_max)
customers_mean = stores_file["Contagem Diária de Clientes"].mean()
print(customers_mean)
customers_std = stores_file["Contagem Diária de Clientes"].std()
print(customers_std)

# Calcular as estatísticas para a coluna Contagem Histórico de Vendas
print('\nHistórico de Vendas:')
sales_min = stores_file["Histórico de Vendas"].min()
print(sales_min)
sales_max = stores_file["Histórico de Vendas"].max()
print(sales_max)
sales_mean = stores_file["Histórico de Vendas"].mean()
print(sales_mean)
sales_std = stores_file["Histórico de Vendas"].std()
print(sales_std)

import matplotlib.pyplot as plt

# Configurar o gráfico 1
plt.bar(stores_file.index, stores_file["Itens Disponíveis"], color = 'red')
plt.title("Itens Disponíveis")
plt.xlabel("Índice")
plt.ylabel("Itens Disponíveis")

# Mostrar o gráfico 1
plt.show()

# Configurar o gráfico 2
plt.bar(stores_file.index, stores_file["Contagem Diária de Clientes"], color = 'green')
plt.title("Contagem Diária de Clientes")
plt.xlabel("Índice")
plt.ylabel("Contagem Diária de Clientes")
plt.show()

# Mostrar o gráfico 2
plt.show()

# Configurar o gráfico 3
plt.bar(stores_file.index, stores_file["Histórico de Vendas"], color = 'blue')
plt.title("Histórico de Vendas")
plt.xlabel("Índice")
plt.ylabel("Vendas em (US$)")
plt.show()

# Mostrar o gráfico 3
plt.show()