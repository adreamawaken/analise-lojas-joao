#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de teste para verificar se o ambiente está configurado corretamente
"""

print("🔧 Testando configuração do ambiente...")

try:
    import pandas as pd
    print("✅ Pandas importado com sucesso")
    
    import matplotlib.pyplot as plt
    print("✅ Matplotlib importado com sucesso")
    
    import seaborn as sns
    print("✅ Seaborn importado com sucesso")
    
    import numpy as np
    print("✅ NumPy importado com sucesso")
    
    # Testar carregamento dos dados
    dados_lojas = pd.read_csv('../data/dados_lojas.csv')
    print(f"✅ Dados das lojas carregados: {len(dados_lojas)} registros")
    
    produtos_detalhados = pd.read_csv('../data/produtos_detalhados.csv')
    print(f"✅ Dados dos produtos carregados: {len(produtos_detalhados)} registros")
    
    print("\n📊 Primeiras linhas dos dados das lojas:")
    print(dados_lojas.head(3))
    
    print("\n🎯 Ambiente configurado corretamente!")
    print("🚀 Execute: python analise_lojas_joao.py")
    
except Exception as e:
    print(f"❌ Erro: {e}")
    print("💡 Verifique se as dependências estão instaladas:")
    print("   pip install pandas matplotlib seaborn numpy")
