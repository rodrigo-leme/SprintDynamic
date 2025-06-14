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




📊 Exemplo de Saída
🔬 SISTEMA DE CONTROLE DE ESTOQUE - DASA PATOLOGIA
============================================================

1️⃣ ANÁLISE DE PRODUTOS EM FALTA (Algoritmo Heap - O(n log k)):
------------------------------------------------------------
⏱️  Tempo de execução com Heap: 0.000245 segundos
📊 Total de produtos em falta: 8

🚨 Top 3 produtos mais críticos:
1. Lâminas_Microscopia em DASA_BA_Salvador
   Criticidade: 40.0%
   Faltam: 60 unidades
   Custo reposição: R$ 51.00

2. Reagente_Hematoxilina em DASA_BA_Salvador
   Criticidade: 62.5%
   Faltam: 5 unidades
   Custo reposição: R$ 725.00
🔍 Considerações Finais
Este sistema resolve os desafios apresentados pela DASA ao:

Eliminar processos manuais propensos a erros
Fornecer visibilidade em tempo real do estoque
Automatizar decisões de reposição e transferência
Otimizar custos através de análises preditivas
Garantir disponibilidade de insumos críticos
