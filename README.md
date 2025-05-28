# Análise de Estoque com Streamlit

![Python](https://img.shields.io/badge/Python-programming%20language-blue?style=flat-square&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat-square&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Plotting-ff4088?style=flat-square&logo=gnuplot&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-4B8BBE?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-ff4b4b?style=flat-square&logo=streamlit&logoColor=white)

## Descrição

Este projeto consiste em uma aplicação web desenvolvida com a biblioteca Streamlit, voltada para análise de dados de estoque de supermercado. O sistema permite ao usuário explorar informações sobre os produtos armazenados, suas quantidades e categorias.

A interface é interativa e responsiva, com uso de filtros laterais para seleção de categorias e quantidade de dados exibidos, além de uma visualização gráfica baseada em gráficos de barras para facilitar a interpretação visual dos dados.

O principal objetivo deste projeto é proporcionar uma ferramenta simples, leve e funcional que auxilie na visualização e interpretação de dados tabulares armazenados em formato CSV, especialmente em contextos de controle de inventário ou supervisão de produtos.

## Funcionalidades

- Carregamento automático de um arquivo `.csv` contendo os dados de estoque.
- Exibição de uma tabela dinâmica com os produtos e suas respectivas informações.
- Filtro de categorias para segmentação dos dados por tipo de produto.
- Controle da quantidade de linhas exibidas na tabela via controle deslizante (slider).
- Geração de gráficos de barras para análise da quantidade de produtos por categoria.
- Atualização dinâmica do gráfico conforme a categoria selecionada.
- Formatação da coluna de valores com duas casas decimais.
- Uso de rótulos ajustados e otimizados para melhor leitura no gráfico.
- Layout limpo com foco na experiência do usuário e na clareza das informações.
- Implementação de boas práticas na organização do código e separação de responsabilidades.

## Tecnologias abordadas

- **Python**: Linguagem principal utilizada para o desenvolvimento do projeto.
- **Pandas**: Utilizada para leitura do arquivo CSV, manipulação e filtragem dos dados.
- **Matplotlib**: Biblioteca de visualização que fornece a base para os gráficos gerados.
- **Seaborn**: Biblioteca complementar ao Matplotlib, responsável por estilizar os gráficos.
- **Streamlit**: Framework web usado para criar a interface gráfica de maneira simples e rápida, facilitando a criação de dashboards e ferramentas de análise interativa.

Este projeto demonstra como é possível construir soluções de visualização de dados eficientes e acessíveis com ferramentas do ecossistema Python, permitindo que profissionais da área de dados, logística ou gestão de estoque tenham insights rápidos sem depender de sistemas complexos.

A aplicação é flexível, podendo ser adaptada para novos conjuntos de dados, outras categorias de produtos ou métricas adicionais. A modularidade e clareza do código também tornam fácil sua expansão futura com novos recursos, como exportação de relatórios ou conexão com bancos de dados.

Combinando análise de dados, visualização e desenvolvimento web, este projeto serve como base prática para quem deseja integrar ciência de dados a soluções visuais de forma direta e funcional.
