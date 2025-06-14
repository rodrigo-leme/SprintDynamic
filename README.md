# Sistema de Gestão de Estoque DASA

##  Descrição
Sistema completo de gestão de estoque desenvolvido para otimizar o controle de insumos nas unidades diagnósticas da DASA, implementando estruturas de dados avançadas e algoritmos otimizados.

##  Funcionalidades 
-  Monitoramento em tempo real de estoque
-  Previsão inteligente de demanda
-  Otimização de distribuição entre unidades
-  Alertas automáticos de reposição
-  Análise de criticidade e priorização
-  Relatórios gerenciais detalhados

##  Tecnologias 
- Python 3.8+
- NumPy (análises estatísticas)
- Matplotlib (visualizações)
- JSON (persistência de dados)

### Pré-requisitos
 
python --version  # Python 3 


Sistema de Controle de Estoque para Laboratório de Patologia 🔬
- sistema de controle de estoque para laboratórios, focando em insumos críticos para análises patológicas.

📋 Visão Geral do Projeto
Este sistema foi desenvolvido para resolver problemas de:

Baixa visibilidade no controle de insumos (Desafio 1)
Gestão manual propensa a erros (relacionado ao Desafio 2)
Falta de rastreabilidade e alertas automatizados

🎯 Hipóteses e Dados Considerados
Hipóteses:
Múltiplas unidades: A DASA possui várias unidades que compartilham insumos
Insumos críticos: Reagentes, lâminas, corantes e EPIs são essenciais
Níveis ideais: Cada unidade tem necessidades específicas baseadas em volume
Consumo variável: O uso varia por unidade e tipo de exame
Lead time: Reposição leva 3-7 dias dependendo do fornecedor
Dados simulados baseados em cenários reais:
5 unidades DASA em diferentes locais
10+ tipos de insumos essenciais
Valores de estoque atual, mínimo e ideal
Preços unitários e fornecedores
