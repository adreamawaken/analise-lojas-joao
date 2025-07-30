#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROJETO: Análise de Lojas do Senhor João
EXECUÇÃO PRINCIPAL

Este script facilita a execução do projeto a partir do diretório raiz.
"""

import sys
import os
import subprocess

def main():
    print("🏪 ANÁLISE DE LOJAS DO SENHOR JOÃO")
    print("=" * 50)
    
    # Verificar se estamos no diretório correto
    if not os.path.exists('src/analise_lojas_joao.py'):
        print("❌ Erro: Execute este script a partir do diretório raiz do projeto")
        return
    
    # Mudar para o diretório src
    os.chdir('src')
    
    try:
        # Executar a análise principal
        subprocess.run([sys.executable, 'analise_lojas_joao.py'], check=True)
        
        print("\n✅ Análise concluída com sucesso!")
        print("📊 Gráficos salvos em: outputs/graficos/")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar análise: {e}")
        print("💡 Tente executar: pip install -r requirements.txt")
    except FileNotFoundError:
        print("❌ Python não encontrado. Verifique se Python está instalado.")

if __name__ == "__main__":
    main()
