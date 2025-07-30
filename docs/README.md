# 🏪 Análise de Dados - Lojas do Senhor João

## 📋 Descrição do Projeto

Este projeto realiza uma análise completa de dados de 20 lojas para auxiliar o **Senhor João** na decisão de qual loja adquirir. A análise é baseada em múltiplos critérios como faturamento, avaliações dos clientes, localização geográfica, categorias de produtos e custos de frete.

## 🎯 Objetivos

1. **Analisar o desempenho** das lojas em diferentes métricas
2. **Criar visualizações** para apresentar os dados de forma clara
3. **Mapear a distribuição geográfica** das vendas
4. **Fornecer uma recomendação** fundamentada em dados

## 📊 Dataset

### `dados_lojas.csv`
Contém informações de 20 lojas distribuídas pelo Brasil:
- **loja_id**: Identificador único da loja
- **nome_loja**: Nome e localização da loja
- **faturamento_mensal**: Receita mensal em R$
- **categoria_principal**: Categoria principal de produtos
- **produtos_vendidos**: Quantidade de produtos vendidos
- **avaliacao_media**: Avaliação média dos clientes (1-5)
- **frete_medio**: Custo médio de frete em R$
- **lat/lon**: Coordenadas geográficas
- **regiao**: Região do Brasil

### `produtos_detalhados.csv`
Detalhamento dos produtos vendidos por loja:
- **loja_id**: ID da loja
- **produto**: Nome do produto
- **categoria**: Categoria do produto
- **quantidade_vendida**: Unidades vendidas
- **preco_unitario**: Preço por unidade
- **receita_produto**: Receita total do produto

## 🔧 Tecnologias Utilizadas

- **Python 3.13**
- **Pandas**: Manipulação e análise de dados
- **Matplotlib**: Criação de gráficos
- **Seaborn**: Visualizações estatísticas
- **NumPy**: Operações numéricas

## 📈 Visualizações Geradas

O projeto gera **6 tipos diferentes** de visualizações:

### 1. 📊 Faturamento por Loja (Gráfico de Barras Horizontais)
- Mostra o ranking de faturamento de todas as lojas
- Valores em R$ formatados para fácil leitura
- Cores gradientes para destacar diferenças

### 2. 🥧 Participação das Categorias (Gráfico de Pizza + Barras)
- Distribuição do faturamento por categoria de produto
- Quantidade de lojas por categoria
- Destaque para a categoria com maior participação

### 3. ⭐ Correlação Avaliação vs Faturamento (Dispersão)
- Relação entre satisfação do cliente e receita
- Pontos coloridos por região
- Linha de tendência e coeficiente de correlação

### 4. 🗺️ Mapa Geográfico de Vendas (Scatter Plot Duplo)
- Distribuição geográfica do faturamento
- Mapa de avaliações por localização
- Tamanho dos pontos proporcional ao faturamento

### 5. 📊 Análise Regional Completa (Painel 2x2)
- Faturamento médio por região
- Avaliação média por região
- Frete médio por região
- Total de produtos vendidos por região

### 6. 🏆 Ranking de Performance (Barras Horizontais)
- Score calculado considerando múltiplos fatores
- Cores por região para identificação
- Ranking final das lojas

## 🚀 Como Executar o Projeto

### Pré-requisitos
```bash
# Verificar se Python está instalado
python --version
```

### 1. Instalar Dependências
```bash
# Instalar bibliotecas necessárias
pip install pandas matplotlib seaborn numpy
```

### 2. Executar a Análise
```bash
# Executar o script principal
python analise_lojas_joao.py
```

### 3. Resultados
Após a execução, serão gerados:
- **6 gráficos em PNG** salvos no diretório
- **Relatório completo** no terminal com:
  - Estatísticas descritivas
  - Insights principais
  - Recomendação final

## 📁 Estrutura dos Arquivos

```
📂 Final Project/
├── 📄 analise_lojas_joao.py     # Script principal
├── 📄 dados_lojas.csv           # Dataset das lojas
├── 📄 produtos_detalhados.csv   # Dataset dos produtos
├── 📄 requirements.txt          # Dependências
├── 📄 README.md                 # Este arquivo
└── 📊 Gráficos gerados:
    ├── grafico_1_faturamento_por_loja.png
    ├── grafico_2_categorias_vendas.png
    ├── grafico_3_avaliacao_vs_faturamento.png
    ├── grafico_4_mapa_geografico.png
    ├── grafico_5_analise_regional.png
    └── grafico_6_ranking_performance.png
```

## 🎯 Metodologia de Análise

### Score de Performance
O algoritmo calcula um score baseado em:
- **40%** - Faturamento normalizado
- **30%** - Avaliação dos clientes
- **30%** - Eficiência do frete (menor custo = melhor score)

### Critérios de Recomendação
1. **Performance Geral** (score calculado)
2. **Equilíbrio** entre faturamento e satisfação
3. **Localização Estratégica**
4. **Potencial da Categoria**

## 📊 Insights Principais

### Distribuição Regional
- **Sudeste**: 8 lojas (40% do total)
- **Nordeste**: 4 lojas (20% do total)
- **Sul**: 4 lojas (20% do total)
- **Centro-Oeste**: 2 lojas (10% do total)
- **Norte**: 2 lojas (10% do total)

### Categorias Mais Representadas
- **Eletrônicos**: Alta margem e faturamento
- **Moda**: Grande volume de vendas
- **Casa e Jardim**: Produtos de ticket médio
- **Esportes**: Nicho especializado
- **Livros**: Menor faturamento, mas público fiel

## 💡 Recomendação Final

Com base na análise completa dos dados, o sistema fornece uma recomendação fundamentada considerando:

✅ **Loja com melhor score de performance**  
✅ **Equilíbrio entre rentabilidade e satisfação**  
✅ **Localização geográfica estratégica**  
✅ **Categoria com potencial de crescimento**  

## 🔍 Próximos Passos

Para aprofundar a análise, considere:
- Análise de sazonalidade das vendas
- Estudo da concorrência local
- Análise de custos operacionais
- Projeção de crescimento futuro
- Integração com mapas interativos (Folium)

## 📞 Contato

Projeto desenvolvido para auxiliar o **Senhor João** na tomada de decisão estratégica baseada em dados.

---
*Análise realizada com Python e bibliotecas de Data Science - Janeiro 2025*
