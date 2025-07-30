# 🚀 GUIA RÁPIDO - Como Visualizar o Projeto

## ⚡ Execução Rápida

### 1. Abrir Terminal no VS Code
```
Ctrl + Shift + ` (ou Terminal > New Terminal)
```

### 2. Navegar para o Diretório (se necessário)
```bash
cd "c:\Users\MANUEL JR\Documents\.Estudos\Oracle + Alura\Data Specialization\Final Project"
```

### 3. Instalar Dependências (apenas uma vez)
```bash
pip install pandas matplotlib seaborn numpy
```

### 4. Executar Análise Completa
```bash
python analise_lojas_joao.py
```

## 📊 O que Acontece Quando Executar

### No Terminal, você verá:
1. ✅ **Confirmação de carregamento** dos dados
2. 📋 **Exploração inicial** - estatísticas básicas
3. 📈 **Mensagem de geração** das visualizações
4. 🏆 **Recomendação final** com justificativa

### Arquivos Gerados:
6 gráficos PNG serão salvos automaticamente:
- `grafico_1_faturamento_por_loja.png`
- `grafico_2_categorias_vendas.png`
- `grafico_3_avaliacao_vs_faturamento.png`
- `grafico_4_mapa_geografico.png`
- `grafico_5_analise_regional.png`
- `grafico_6_ranking_performance.png`

## 🎯 Interpretando os Resultados

### Score de Performance
O algoritmo calcula um score de 0 a 1 considerando:
- **Faturamento**: Quanto maior, melhor
- **Avaliação**: Quanto mais próximo de 5, melhor
- **Frete**: Quanto menor, melhor

### Recomendação Final
A loja recomendada será aquela com:
- ✅ Maior score de performance geral
- ✅ Melhor equilíbrio entre todos os fatores
- ✅ Localização estratégica

## 🔧 Solução de Problemas

### Erro: "No module named 'pandas'"
```bash
pip install pandas matplotlib seaborn numpy
```

### Erro: "File not found"
Certifique-se de estar no diretório correto:
```bash
ls  # Linux/Mac
dir # Windows
```
Você deve ver os arquivos:
- analise_lojas_joao.py
- dados_lojas.csv
- produtos_detalhados.csv

### Gráficos não aparecem
Os gráficos são salvos como PNG no mesmo diretório. Para visualizar:
1. Abra o Explorer do VS Code
2. Clique nos arquivos PNG gerados
3. Use a prévia do VS Code para ver as imagens

## 📱 Visualização no VS Code

### Para ver os gráficos:
1. **Painel Explorer** (Ctrl+Shift+E)
2. **Clique nos arquivos PNG**
3. VS Code abrirá uma prévia automática

### Para análise completa:
1. **Execute o script**
2. **Leia o output do terminal**
3. **Visualize os gráficos gerados**
4. **Consulte o README.md para interpretação**

---
💡 **Dica**: Execute `python test_setup.py` primeiro para verificar se tudo está configurado corretamente!
