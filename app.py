import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Função para exibir um numero configuravel de linhas da tabela
def mostra_qntd_linhas(dataframe):
  qntd_linhas = st.sidebar.slider(
    "Selecione a quantidade de linhas que deseja mostrar na tabela",
    min_value=1,
    max_value=len(dataframe),
    step=1,
  )
  # Exibe a tabela formatando a coluna 'Valor' com duas casas decimais
  st.write(
    dataframe.head(qntd_linhas).style.format(subset=['Valor'], formatter="{:.2f}")
  )

# Função para criar gráfico de barras da quantidade por produto, filtrado por categoria
def plot_estoque(dataframe, categoria):
  dados_plot = dataframe.query('Categoria == @categoria')

  fig, ax = plt.subplots(figsize=(12, 6))
  sns.barplot(
    data=dados_plot,
    x='Produto',
    y='Quantidade',
    ax=ax,
  )
  ax.set_title(f'Quantidade em estoque dos produtos de {categoria}', fontsize=16)
  ax.set_xlabel('Produtos', fontsize=14)
  ax.set_ylabel('Quantidade', fontsize=14)
  ax.tick_params(axis='x', rotation=60, labelsize=8)

  return fig

# Carrega os dados do arquivo CSV
dados = pd.read_csv('estoque.csv')

# Titulo e introdução
st.title('Análise de Estoque')
st.write(
  'Nesse projeto vamos analisar a quantidade de produtos em estoque, por categoria, '
  'de uma base de dados de produtos de supermercado.'
)

# Filtro e exibição da tabela
opcao_1 = st.sidebar.checkbox("Mostrar tabela de produtos")

if opcao_1:
  st.sidebar.markdown("## Filtro para a tabela")

  categorias = list(dados['Categoria'].unique())
  categorias.append('Todas')

  categoria_selecionada = st.sidebar.selectbox(
    "Selecione a categoria para apresentação na tabela",
    options=categorias,
  )

  if categoria_selecionada != 'Todas':
    df_categoria = dados.query('Categoria == @categoria_selecionada')
    mostra_qntd_linhas(df_categoria)
  else:
    mostra_qntd_linhas(dados)

# Filtro e exibição do gráfico
st.sidebar.markdown("## Filtro para o gráfico")

categoria_grafico = st.sidebar.selectbox(
    "Selecione a categoria para apresentar no gráfico",
    options=dados['Categoria'].unique(),
)

figura = plot_estoque(dados, categoria_grafico)
st.pyplot(figura)

