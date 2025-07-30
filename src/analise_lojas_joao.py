import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.patches import Patch
import warnings
warnings.filterwarnings('ignore')

# Configurações de estilo
plt.style.use('default')
sns.set_theme()
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

class AnaliseLojasJoao:
    def __init__(self):
        """Inicializa a classe de análise das lojas"""
        self.dados_lojas = None
        self.produtos_detalhados = None
        self.load_data()
        
    def load_data(self):
        """Carrega os dados dos arquivos CSV"""
        try:
            self.dados_lojas = pd.read_csv('../data/dados_lojas.csv')
            self.produtos_detalhados = pd.read_csv('../data/produtos_detalhados.csv')
            print("✅ Dados carregados com sucesso!")
            print(f"📊 Total de lojas: {len(self.dados_lojas)}")
            print(f"📦 Total de produtos detalhados: {len(self.produtos_detalhados)}")
        except FileNotFoundError as e:
            print(f"❌ Erro ao carregar dados: {e}")
            print("💡 Certifique-se de que os arquivos CSV estão na pasta 'data/'")
            
    def explorar_dados(self):
        """Exibe informações básicas sobre os dados"""
        print("\n" + "="*50)
        print("📋 EXPLORAÇÃO INICIAL DOS DADOS")
        print("="*50)
        
        print("\n📈 Informações das Lojas:")
        print(self.dados_lojas.info())
        
        print("\n📊 Estatísticas Descritivas - Faturamento:")
        print(self.dados_lojas[['faturamento_mensal', 'produtos_vendidos', 'avaliacao_media', 'frete_medio']].describe())
        
        print("\n🏪 Distribuição por Região:")
        print(self.dados_lojas['regiao'].value_counts())
        
        print("\n🛍️ Distribuição por Categoria:")
        print(self.dados_lojas['categoria_principal'].value_counts())
        
    def grafico_faturamento_por_loja(self):
        """Gráfico 1: Faturamento por loja (Gráfico de Barras)"""
        fig, ax = plt.subplots(figsize=(15, 8))
        
        # Ordenar por faturamento
        dados_ordenados = self.dados_lojas.sort_values('faturamento_mensal', ascending=True)
        
        bars = ax.barh(dados_ordenados['nome_loja'], dados_ordenados['faturamento_mensal'], 
                       color=sns.color_palette("viridis", len(dados_ordenados)))
        
        # Adicionar valores nas barras
        for i, bar in enumerate(bars):
            width = bar.get_width()
            ax.text(width + 2000, bar.get_y() + bar.get_height()/2, 
                   f'R$ {width:,.0f}', ha='left', va='center', fontweight='bold')
        
        ax.set_xlabel('Faturamento Mensal (R$)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Lojas', fontsize=12, fontweight='bold')
        ax.set_title('💰 Faturamento Mensal por Loja\n(Ordenado do menor para o maior)', 
                    fontsize=14, fontweight='bold', pad=20)
        
        # Formatação do eixo x
        ax.ticklabel_format(style='plain', axis='x')
        ax.grid(axis='x', alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('../outputs/graficos/grafico_1_faturamento_por_loja.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def grafico_categoria_vendas(self):
        """Gráfico 2: Participação das categorias no faturamento total (Gráfico de Pizza)"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))
        
        # Gráfico de Pizza - Faturamento por Categoria
        faturamento_categoria = self.dados_lojas.groupby('categoria_principal')['faturamento_mensal'].sum()
        
        colors = plt.cm.Set3(np.linspace(0, 1, len(faturamento_categoria)))
        wedges, texts, autotexts = ax1.pie(faturamento_categoria.values, 
                                          labels=faturamento_categoria.index,
                                          autopct='%1.1f%%',
                                          colors=colors,
                                          explode=[0.05 if cat == faturamento_categoria.idxmax() else 0 
                                                  for cat in faturamento_categoria.index],
                                          shadow=True,
                                          startangle=90)
        
        ax1.set_title('🏪 Participação das Categorias no Faturamento Total', 
                     fontsize=14, fontweight='bold', pad=20)
        
        # Melhorar a aparência dos textos
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(10)
        
        # Gráfico de Barras - Quantidade de Lojas por Categoria
        categoria_count = self.dados_lojas['categoria_principal'].value_counts()
        bars = ax2.bar(categoria_count.index, categoria_count.values, 
                       color=sns.color_palette("husl", len(categoria_count)))
        
        ax2.set_title('📊 Quantidade de Lojas por Categoria', 
                     fontsize=14, fontweight='bold', pad=20)
        ax2.set_xlabel('Categoria', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Número de Lojas', fontsize=12, fontweight='bold')
        
        # Adicionar valores nas barras
        for bar in bars:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                    f'{int(height)}', ha='center', va='bottom', fontweight='bold')
        
        ax2.grid(axis='y', alpha=0.3)
        plt.xticks(rotation=45)
        
        plt.tight_layout()
        plt.savefig('../outputs/graficos/grafico_2_categorias_vendas.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def grafico_avaliacao_vs_faturamento(self):
        """Gráfico 3: Correlação entre Avaliação e Faturamento (Gráfico de Dispersão)"""
        fig, ax = plt.subplots(figsize=(14, 8))
        
        # Criar o scatter plot com cores por região
        regioes = self.dados_lojas['regiao'].unique()
        colors = plt.cm.tab10(np.linspace(0, 1, len(regioes)))
        
        for i, regiao in enumerate(regioes):
            dados_regiao = self.dados_lojas[self.dados_lojas['regiao'] == regiao]
            ax.scatter(dados_regiao['avaliacao_media'], dados_regiao['faturamento_mensal'],
                      c=[colors[i]], label=regiao, s=100, alpha=0.7, edgecolors='black', linewidth=1)
        
        # Adicionar linha de tendência
        z = np.polyfit(self.dados_lojas['avaliacao_media'], self.dados_lojas['faturamento_mensal'], 1)
        p = np.poly1d(z)
        ax.plot(self.dados_lojas['avaliacao_media'], p(self.dados_lojas['avaliacao_media']), 
                "r--", alpha=0.8, linewidth=2, label='Linha de Tendência')
        
        # Calcular correlação
        correlacao = self.dados_lojas['avaliacao_media'].corr(self.dados_lojas['faturamento_mensal'])
        
        ax.set_xlabel('Avaliação Média (⭐)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Faturamento Mensal (R$)', fontsize=12, fontweight='bold')
        ax.set_title(f'⭐ Correlação entre Avaliação e Faturamento\n(Correlação: {correlacao:.3f})', 
                    fontsize=14, fontweight='bold', pad=20)
        
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.grid(True, alpha=0.3)
        
        # Formatação do eixo y
        ax.ticklabel_format(style='plain', axis='y')
        
        plt.tight_layout()
        plt.savefig('../outputs/graficos/grafico_3_avaliacao_vs_faturamento.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def mapa_geografico_vendas(self):
        """Gráfico 4: Mapa de Vendas por Localização Geográfica"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))
        
        # Mapa de Dispersão - Faturamento por Localização
        scatter = ax1.scatter(self.dados_lojas['lon'], self.dados_lojas['lat'], 
                             c=self.dados_lojas['faturamento_mensal'],
                             s=self.dados_lojas['faturamento_mensal']/1000,
                             cmap='viridis', alpha=0.7, edgecolors='black', linewidth=1)
        
        ax1.set_xlabel('Longitude', fontsize=12, fontweight='bold')
        ax1.set_ylabel('Latitude', fontsize=12, fontweight='bold')
        ax1.set_title('🗺️ Distribuição Geográfica do Faturamento\n(Tamanho do ponto = Faturamento)', 
                     fontsize=14, fontweight='bold', pad=20)
        
        # Adicionar colorbar
        cbar1 = plt.colorbar(scatter, ax=ax1, shrink=0.8)
        cbar1.set_label('Faturamento (R$)', fontweight='bold')
        
        # Mapa de Dispersão - Avaliação por Localização
        scatter2 = ax2.scatter(self.dados_lojas['lon'], self.dados_lojas['lat'], 
                              c=self.dados_lojas['avaliacao_media'],
                              s=200, cmap='RdYlGn', alpha=0.7, edgecolors='black', linewidth=1)
        
        ax2.set_xlabel('Longitude', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Latitude', fontsize=12, fontweight='bold')
        ax2.set_title('⭐ Distribuição Geográfica das Avaliações', 
                     fontsize=14, fontweight='bold', pad=20)
        
        # Adicionar colorbar
        cbar2 = plt.colorbar(scatter2, ax=ax2, shrink=0.8)
        cbar2.set_label('Avaliação Média', fontweight='bold')
        
        plt.tight_layout()
        plt.savefig('../outputs/graficos/grafico_4_mapa_geografico.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def analise_regional_completa(self):
        """Gráfico 5: Análise Completa por Região"""
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(18, 12))
        
        # 1. Faturamento Médio por Região
        faturamento_regiao = self.dados_lojas.groupby('regiao')['faturamento_mensal'].agg(['mean', 'sum', 'count'])
        
        bars1 = ax1.bar(faturamento_regiao.index, faturamento_regiao['mean'], 
                       color=sns.color_palette("viridis", len(faturamento_regiao)))
        ax1.set_title('💰 Faturamento Médio por Região', fontweight='bold', fontsize=12)
        ax1.set_ylabel('Faturamento Médio (R$)', fontweight='bold')
        ax1.tick_params(axis='x', rotation=45)
        
        for bar in bars1:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height + 1000,
                    f'R$ {height:,.0f}', ha='center', va='bottom', fontweight='bold', fontsize=9)
        
        # 2. Avaliação Média por Região
        avaliacao_regiao = self.dados_lojas.groupby('regiao')['avaliacao_media'].mean()
        bars2 = ax2.bar(avaliacao_regiao.index, avaliacao_regiao.values, 
                       color=sns.color_palette("plasma", len(avaliacao_regiao)))
        ax2.set_title('⭐ Avaliação Média por Região', fontweight='bold', fontsize=12)
        ax2.set_ylabel('Avaliação Média', fontweight='bold')
        ax2.tick_params(axis='x', rotation=45)
        ax2.set_ylim(3.5, 5.0)
        
        for bar in bars2:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height + 0.02,
                    f'{height:.2f}', ha='center', va='bottom', fontweight='bold', fontsize=9)
        
        # 3. Frete Médio por Região
        frete_regiao = self.dados_lojas.groupby('regiao')['frete_medio'].mean()
        bars3 = ax3.bar(frete_regiao.index, frete_regiao.values, 
                       color=sns.color_palette("coolwarm", len(frete_regiao)))
        ax3.set_title('🚚 Frete Médio por Região', fontweight='bold', fontsize=12)
        ax3.set_ylabel('Frete Médio (R$)', fontweight='bold')
        ax3.tick_params(axis='x', rotation=45)
        
        for bar in bars3:
            height = bar.get_height()
            ax3.text(bar.get_x() + bar.get_width()/2., height + 0.2,
                    f'R$ {height:.2f}', ha='center', va='bottom', fontweight='bold', fontsize=9)
        
        # 4. Produtos Vendidos por Região
        produtos_regiao = self.dados_lojas.groupby('regiao')['produtos_vendidos'].sum()
        bars4 = ax4.bar(produtos_regiao.index, produtos_regiao.values, 
                       color=sns.color_palette("Set2", len(produtos_regiao)))
        ax4.set_title('📦 Total de Produtos Vendidos por Região', fontweight='bold', fontsize=12)
        ax4.set_ylabel('Produtos Vendidos', fontweight='bold')
        ax4.tick_params(axis='x', rotation=45)
        
        for bar in bars4:
            height = bar.get_height()
            ax4.text(bar.get_x() + bar.get_width()/2., height + 50,
                    f'{int(height)}', ha='center', va='bottom', fontweight='bold', fontsize=9)
        
        plt.suptitle('📊 ANÁLISE COMPLETA POR REGIÃO', fontsize=16, fontweight='bold', y=0.98)
        plt.tight_layout()
        plt.savefig('../outputs/graficos/grafico_5_analise_regional.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def ranking_lojas_performance(self):
        """Gráfico 6: Ranking de Performance das Lojas"""
        # Criar score de performance baseado em múltiplos fatores
        self.dados_lojas['score_performance'] = (
            (self.dados_lojas['faturamento_mensal'] / self.dados_lojas['faturamento_mensal'].max() * 0.4) +
            (self.dados_lojas['avaliacao_media'] / 5.0 * 0.3) +
            ((self.dados_lojas['frete_medio'].max() - self.dados_lojas['frete_medio']) / self.dados_lojas['frete_medio'].max() * 0.3)  # Inverso do frete (menor é melhor)
        )
        
        fig, ax = plt.subplots(figsize=(16, 10))
        
        # Ordenar por score de performance
        dados_ranking = self.dados_lojas.sort_values('score_performance', ascending=True)
        
        # Criar cores baseadas na região
        region_colors = {'Sudeste': '#1f77b4', 'Nordeste': '#ff7f0e', 'Sul': '#2ca02c', 
                        'Centro-Oeste': '#d62728', 'Norte': '#9467bd'}
        colors = [region_colors[region] for region in dados_ranking['regiao']]
        
        bars = ax.barh(range(len(dados_ranking)), dados_ranking['score_performance'], 
                       color=colors, alpha=0.8, edgecolor='black', linewidth=0.5)
        
        # Personalizar eixos
        ax.set_yticks(range(len(dados_ranking)))
        ax.set_yticklabels(dados_ranking['nome_loja'], fontsize=10)
        ax.set_xlabel('Score de Performance', fontsize=12, fontweight='bold')
        ax.set_title('🏆 RANKING DE PERFORMANCE DAS LOJAS\n(Baseado em Faturamento, Avaliação e Frete)', 
                    fontsize=14, fontweight='bold', pad=20)
        
        # Adicionar valores nas barras
        for i, bar in enumerate(bars):
            width = bar.get_width()
            ax.text(width + 0.01, bar.get_y() + bar.get_height()/2, 
                   f'{width:.3f}', ha='left', va='center', fontweight='bold', fontsize=9)
        
        # Adicionar legenda das regiões
        legend_elements = [Patch(facecolor=color, label=region) 
                          for region, color in region_colors.items()]
        ax.legend(handles=legend_elements, loc='lower right', title='Regiões', title_fontsize=12)
        
        ax.grid(axis='x', alpha=0.3)
        plt.tight_layout()
        plt.savefig('../outputs/graficos/grafico_6_ranking_performance.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def gerar_relatorio_completo(self):
        """Gera todas as análises e recomendações"""
        print("\n" + "="*70)
        print("🏪 ANÁLISE COMPLETA DAS LOJAS - SENHOR JOÃO")
        print("="*70)
        
        # Explorar dados
        self.explorar_dados()
        
        # Gerar todos os gráficos
        print("\n📈 Gerando visualizações...")
        self.grafico_faturamento_por_loja()
        self.grafico_categoria_vendas()
        self.grafico_avaliacao_vs_faturamento()
        self.mapa_geografico_vendas()
        self.analise_regional_completa()
        self.ranking_lojas_performance()
        
        # Análises e recomendações
        self.gerar_recomendacoes()
        
    def gerar_recomendacoes(self):
        """Gera recomendações baseadas na análise dos dados"""
        print("\n" + "="*70)
        print("💡 RECOMENDAÇÕES PARA O SENHOR JOÃO")
        print("="*70)
        
        # Encontrar a melhor loja
        melhor_loja = self.dados_lojas.loc[self.dados_lojas['score_performance'].idxmax()]
        
        print(f"\n🏆 LOJA RECOMENDADA: {melhor_loja['nome_loja']}")
        print(f"📍 Localização: {melhor_loja['nome_loja']}")
        print(f"💰 Faturamento Mensal: R$ {melhor_loja['faturamento_mensal']:,.2f}")
        print(f"⭐ Avaliação Média: {melhor_loja['avaliacao_media']}/5.0")
        print(f"🚚 Frete Médio: R$ {melhor_loja['frete_medio']:.2f}")
        print(f"📦 Produtos Vendidos: {melhor_loja['produtos_vendidos']}")
        print(f"🏪 Categoria Principal: {melhor_loja['categoria_principal']}")
        
        print(f"\n📊 JUSTIFICATIVA DA RECOMENDAÇÃO:")
        print(f"• Score de Performance: {melhor_loja['score_performance']:.3f}")
        print(f"• Região estratégica: {melhor_loja['regiao']}")
        
        # Análises adicionais
        print(f"\n📈 INSIGHTS PRINCIPAIS:")
        
        # Top 3 lojas por faturamento
        top_faturamento = self.dados_lojas.nlargest(3, 'faturamento_mensal')
        print(f"\n💰 TOP 3 FATURAMENTO:")
        for i, loja in top_faturamento.iterrows():
            print(f"   {loja['nome_loja']}: R$ {loja['faturamento_mensal']:,.2f}")
        
        # Top 3 lojas por avaliação
        top_avaliacao = self.dados_lojas.nlargest(3, 'avaliacao_media')
        print(f"\n⭐ TOP 3 AVALIAÇÃO:")
        for i, loja in top_avaliacao.iterrows():
            print(f"   {loja['nome_loja']}: {loja['avaliacao_media']}/5.0")
        
        # Análise por região
        print(f"\n🗺️ ANÁLISE GEOGRÁFICA:")
        regiao_stats = self.dados_lojas.groupby('regiao').agg({
            'faturamento_mensal': 'mean',
            'avaliacao_media': 'mean',
            'frete_medio': 'mean'
        }).round(2)
        
        melhor_regiao = regiao_stats.loc[regiao_stats['faturamento_mensal'].idxmax()]
        print(f"   Melhor região por faturamento: {regiao_stats['faturamento_mensal'].idxmax()}")
        print(f"   Faturamento médio: R$ {melhor_regiao['faturamento_mensal']:,.2f}")
        
        print(f"\n✅ CONCLUSÃO FINAL:")
        print(f"   Recomendamos a aquisição da {melhor_loja['nome_loja']} por apresentar:")
        print(f"   • Excelente performance geral (score: {melhor_loja['score_performance']:.3f})")
        print(f"   • Bom equilíbrio entre faturamento e satisfação do cliente")
        print(f"   • Localização estratégica na região {melhor_loja['regiao']}")
        print(f"   • Categoria {melhor_loja['categoria_principal']} com bom potencial")

# Executar análise completa
if __name__ == "__main__":
    analise = AnaliseLojasJoao()
    analise.gerar_relatorio_completo()
