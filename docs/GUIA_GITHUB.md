# 🚀 GUIA: Como Exportar o Projeto para o GitHub

## 📋 Pré-requisitos

### 1. Git Instalado
```bash
# Verificar se Git está instalado
git --version
```
Se não estiver instalado, baixe em: https://git-scm.com/

### 2. Conta no GitHub
- Crie uma conta em: https://github.com
- Opcionalmente, configure SSH keys para facilitar o processo

## 🎯 Passo a Passo Completo

### **PASSO 1: Inicializar Repositório Local**

```bash
# Navegar para o diretório do projeto
cd "c:\Users\MANUEL JR\Documents\.Estudos\Oracle + Alura\Data Specialization\Final Project"

# Inicializar repositório Git
git init

# Configurar informações do usuário (se não configurado globalmente)
git config user.name "Seu Nome"
git config user.email "seu.email@exemplo.com"
```

### **PASSO 2: Adicionar Arquivos ao Repositório**

```bash
# Adicionar todos os arquivos ao staging
git add .

# Verificar status dos arquivos
git status

# Fazer o primeiro commit
git commit -m "🏪 Projeto: Análise de Lojas do Senhor João

- Análise completa de 20 lojas com dados reais
- 6 visualizações diferentes (barras, pizza, dispersão, mapas)
- Sistema de score de performance
- Recomendação fundamentada em dados
- Estrutura profissional organizizada"
```

### **PASSO 3: Criar Repositório no GitHub**

1. **Acesse**: https://github.com
2. **Clique**: "New repository" (botão verde)
3. **Nome**: `analise-lojas-joao` (ou nome de sua escolha)
4. **Descrição**: `🏪 Análise de dados para decisão de compra de lojas - Python, Pandas, Matplotlib`
5. **Público/Privado**: Escolha conforme preferência
6. **NÃO marque**: "Add a README file" (já temos um)
7. **Clique**: "Create repository"

### **PASSO 4: Conectar e Enviar ao GitHub**

```bash
# Adicionar repositório remoto (substitua SEU_USUARIO pelo seu username)
git remote add origin https://github.com/SEU_USUARIO/analise-lojas-joao.git

# Definir branch principal
git branch -M main

# Enviar código para o GitHub
git push -u origin main
```

## 🔐 Alternativa com SSH (Mais Seguro)

Se você configurou chaves SSH:

```bash
# Usar SSH em vez de HTTPS
git remote add origin git@github.com:SEU_USUARIO/analise-lojas-joao.git
git push -u origin main
```

## 📝 Comandos para Atualizações Futuras

Após fazer alterações no projeto:

```bash
# Verificar mudanças
git status

# Adicionar mudanças
git add .

# Commitar mudanças
git commit -m "✨ Descrição das mudanças realizadas"

# Enviar para o GitHub
git push
```

## 🎨 Exemplo de Comandos Completos

```bash
# 1. Navegar para o projeto
cd "c:\Users\MANUEL JR\Documents\.Estudos\Oracle + Alura\Data Specialization\Final Project"

# 2. Inicializar Git
git init

# 3. Configurar usuário (se necessário)
git config user.name "Manuel Jr"
git config user.email "manuel@exemplo.com"

# 4. Adicionar arquivos
git add .

# 5. Primeiro commit
git commit -m "🏪 Projeto inicial: Análise de Lojas do Senhor João

- Dataset com 20 lojas e produtos detalhados
- 6 tipos de visualizações (barras, pizza, scatter, mapas)
- Análise geográfica e regional
- Sistema de ranking por performance
- Recomendação baseada em múltiplos critérios
- Estrutura profissional organizada"

# 6. Conectar ao GitHub (substitua SEU_USUARIO)
git remote add origin https://github.com/SEU_USUARIO/analise-lojas-joao.git

# 7. Enviar para o GitHub
git branch -M main
git push -u origin main
```

## 📊 Estrutura que Será Enviada

```
📂 Repositório GitHub/
├── 📄 README.md                      # Página principal do repo
├── 📄 .gitignore                     # Arquivos ignorados
├── 📄 run_analysis.py                # Script principal
├── 📄 requirements.txt               # Dependências
├── 📄 ORGANIZACAO_CONCLUIDA.md      # Guia de organização
│
├── 📁 data/                          # Dados
│   ├── dados_lojas.csv
│   └── produtos_detalhados.csv
│
├── 📁 src/                           # Código fonte
│   ├── analise_lojas_joao.py
│   └── test_setup.py
│
├── 📁 outputs/                       # Resultados
│   └── graficos/ (6 gráficos PNG)
│
└── 📁 docs/                          # Documentação
    ├── README.md
    └── GUIA_EXECUCAO.md
```

## 🔧 Solução de Problemas

### Erro: "Repository not found"
```bash
# Verificar se o repositório foi criado no GitHub
# Verificar se o nome do usuário está correto na URL
```

### Erro: "Permission denied"
```bash
# Verificar credenciais
git config --list

# Ou usar token de acesso pessoal em vez da senha
```

### Arquivo muito grande
```bash
# Verificar arquivos grandes
git ls-files --others --ignored --exclude-standard

# Adicionar ao .gitignore se necessário
```

## ✅ Verificação Final

Após enviar, verifique:

1. **Acesse seu repositório** no GitHub
2. **Verifique se todos os arquivos** estão lá
3. **README.md** deve aparecer formatado na página
4. **Gráficos** devem estar visíveis na pasta outputs/graficos

## 🌟 Dicas Extras

### Para tornar o repositório mais atrativo:

1. **Tags/Topics** no GitHub:
   - `python`, `data-science`, `pandas`, `matplotlib`, `data-analysis`

2. **Descrição do repositório**:
   - "🏪 Análise de dados para decisão de compra de lojas usando Python, Pandas e Matplotlib"

3. **README badges** (opcional):
   - Python version, license, etc.

---
🎯 **Seu projeto estará profissionalmente disponível no GitHub!** 🚀
