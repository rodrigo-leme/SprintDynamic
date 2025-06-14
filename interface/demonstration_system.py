from business_logic.stock_management import SistemaGestaoEstoque
from business_logic.data_analysis import AnalisadorDados
from algorithms.data_structures import ArvoreAVL, MinHeap, Grafo
from algorithms.sorting_and_searching import SortingAndSearching
import random
import time
import sys

class DemonstracaoSistema:
    """
    classe principal para demonstrar as funcionalidades do sistema DASA,
    incluindo gestão de estoque, estruturas de dados e algoritmos.
    """
    def __init__(self):
        self.sistema = SistemaGestaoEstoque()
        self.analisador = AnalisadorDados(self.sistema)
        self.sorting_and_searching = SortingAndSearching()  

    def demonstrar_sistema(self):
        """Demonstra as funcionalidades principais do sistema de gestão de estoque."""
        print("DEMONSTRAÇÃO: SISTEMA DE GESTÃO DE ESTOQUE DASA")
        print("="*60)
        
        print("\n1. REGISTRO DE CONSUMO E REABASTECIMENTO")
        print("-" * 40)
        self.sistema.reabastecer("UN1", "Luvas", 200)
        self.sistema.reabastecer("UN2", "Máscaras", 150)
        self.sistema.registrar_consumo("UN1", "Luvas", 30)
        self.sistema.registrar_consumo("UN1", "Luvas", 50)
        self.sistema.registrar_consumo("UN2", "Máscaras", 70)
        
        print("\n2. CONSULTA DE ESTOQUE")
        print("-" * 40)
        self.sistema.consultar_estoque("UN1", "Luvas")
        self.sistema.consultar_estoque("UN2")
        
        print("\n3. SISTEMA DE ALERTAS")
        print("-" * 40)
        self.sistema.definir_limite_minimo("UN1", "Luvas", 100)
        self.sistema.registrar_consumo("UN1", "Luvas", 80) 
        self.sistema.verificar_alertas()
        
        print("\n4. ANÁLISE PREDITIVA E OTIMIZAÇÃO")
        print("-" * 40)
        self.analisador.analisar_padroes_consumo()
        self.analisador.prever_necessidades_futuras()
        
        self.sistema.reabastecer("UN1", "Reagente A", 500)
        self.sistema.reabastecer("UN2", "Reagente A", 100)
        self.sistema.registrar_consumo("UN1", "Reagente A", 200)
        self.sistema.registrar_consumo("UN2", "Reagente A", 50)

        transferencias = self.analisador.otimizar_distribuicao_entre_unidades()
        if transferencias:
            for t in transferencias:
                self.analisador.transferir_entre_unidades(
                    t['origem'], t['destino'], t['material'], t['quantidade']
                )

    def demonstrar_estruturas_dados(self):
        print("\n" + "="*60)
        print("DEMONSTRAÇÃO: ESTRUTURAS DE DADOS IMPLEMENTADAS")
        print("="*60)
        
        print("\n1. ÁRVORE AVL - Busca Otimizada de Materiais")
        print("-" * 40)
        
        materiais_demo = [
            ("Reagente A", 100),
            ("Reagente B", 50),
            ("Reagente C", 150),
            ("Reagente D", 75)
        ]
        
        arvore = ArvoreAVL()
        for nome, qtd in materiais_demo:
            arvore.inserir(nome, qtd)
        
        print("Materiais inseridos na árvore AVL:")
        for nome, qtd in materiais_demo:
            print(f"  - {nome}: {qtd} unidades")
        
        print("\nBusca por 'Reagente B':")
        resultado = arvore.buscar("Reagente B")
        if resultado:
            print(f"  ✓ Encontrado: {resultado.chave} com {resultado.valor} unidades")
        
        print("\nTravessia em-ordem (ordem alfabética):")
        arvore.travessia_em_ordem(arvore.raiz)
        
        print("\n\n2. MIN-HEAP - Fila de Prioridade para Reposição")
        print("-" * 40)
        
        heap = MinHeap()
        prioridades = [
            (10, "Luvas - Crítico"),
            (30, "Seringas - Médio"),
            (5, "Reagente X - Urgente"),
            (25, "Álcool - Baixo")
        ]
        
        print("Inserindo itens com prioridades:")
        for prio, item in prioridades:
            heap.inserir(prio, item)
            print(f"  - Prioridade {prio}: {item}")
        
        print("\nExtraindo itens por ordem de prioridade:")
        while heap.tamanho > 0:
            prio, item = heap.extrair_minimo()
            print(f"  → Prioridade {prio}: {item}")
        
        print("\n\n3. GRAFO - Rede de Distribuição entre Unidades")
        print("-" * 40)
        
        grafo = Grafo()
        unidades = ["Central", "Norte", "Sul", "Leste", "Oeste"]
        
        for unidade in unidades:
            grafo.adicionar_vertice(unidade)
        
        conexoes = [
            ("Central", "Norte", 10),
            ("Central", "Sul", 15),
            ("Central", "Leste", 12),
            ("Central", "Oeste", 8),
            ("Norte", "Leste", 7),
            ("Sul", "Oeste", 9),
            ("Leste", "Sul", 11)
        ]
        
        print("Conexões entre unidades:")
        for origem, destino, dist in conexoes:
            grafo.adicionar_aresta(origem, destino, dist)
            print(f"  - {origem} ↔ {destino}: {dist} km")
        
        print("\nCaminho mais curto de 'Norte' para 'Sul':")
        distancias = grafo.dijkstra("Norte")
        if "Sul" in distancias:
            print(f"  → Distância mínima: {distancias['Sul']} km")
        
        print("\nBusca em largura a partir de 'Central':")
        visitados = grafo.bfs("Central")
        print(f"  → Ordem de visita: {' → '.join(visitados)}")

    def demonstrar_algoritmos(self):
        """Demonstra algoritmos implementados"""
        print("\n" + "="*60)
        print("DEMONSTRAÇÃO: ALGORITMOS IMPLEMENTADOS")
        print("="*60)
        
        print("\n1. ALGORITMOS DE ORDENAÇÃO")
        print("-" * 40)
        
        consumos = [45, 12, 78, 34, 89, 23, 56, 67, 90, 11]
        print(f"Array original de consumos: {consumos}")
        
        print("\nQuick Sort:")
        arr_quick = consumos.copy()
        self.sorting_and_searching._quick_sort(arr_quick, 0, len(arr_quick) - 1)
        print(f"  Resultado: {arr_quick}")
        
        print("\nMerge Sort:")
        arr_merge = consumos.copy()
        self.sorting_and_searching._merge_sort(arr_merge)
        print(f"  Resultado: {arr_merge}")
        
        print("\n\n2. BUSCA BINÁRIA")
        print("-" * 40)
        print(f"Array ordenado: {arr_quick}")
        buscar = 56
        indice = self.sorting_and_searching._busca_binaria(arr_quick, buscar)
        if indice != -1:
            print(f"Valor {buscar} encontrado no índice: {indice}")
        
        print("\n\n3. ANÁLISE DE COMPLEXIDADE (Big O)")
        print("-" * 40)
        self._demonstrar_complexidade()
        
        print("\n\n4. PROGRAMAÇÃO DINÂMICA - OTIMIZAÇÃO DE PEDIDOS")
        print("-" * 40)
        self._demonstrar_memoizacao()

    def _demonstrar_complexidade(self):
        """Demonstra análise de complexidade"""
        complexidades = [
            ("Busca Linear", "O(n)", "Percorre todos elementos"),
            ("Busca Binária", "O(log n)", "Divide o espaço de busca pela metade"),
            ("Quick Sort (médio)", "O(n log n)", "Divide e conquista eficiente"),
            ("Quick Sort (pior)", "O(n²)", "Quando o pivot é sempre o menor/maior"),
            ("Merge Sort", "O(n log n)", "Sempre divide ao meio"),
            ("Inserção AVL", "O(log n)", "Árvore sempre balanceada"),
            ("Dijkstra", "O((V + E) log V)", "Com heap binário")
        ]
        
        print("Complexidades dos algoritmos implementados:")
        for algo, complex, desc in complexidades:
            print(f"  • {algo}: {complex}")
            print(f"    → {desc}")
    
    def _demonstrar_memoizacao(self):
        """Demonstra otimização com memoização"""
        print("Problema: Calcular quantidade ótima de pedido considerando descontos")
        print("por volume e minimizando custo total (compra + armazenamento)")
        
        memo = {}
        
        def calcular_custo_otimo(quantidade, preco_unitario=10, custo_armazenagem=0.5):
            """Calcula custo ótimo com memoização"""
            if quantidade in memo:
                return memo[quantidade]
            
            if quantidade >= 1000:
                desconto = 0.15
            elif quantidade >= 500:
                desconto = 0.10
            elif quantidade >= 100:
                desconto = 0.05
            else:
                desconto = 0
            
            custo_compra = quantidade * preco_unitario * (1 - desconto)
            custo_estoque = quantidade * custo_armazenagem * 30  
            custo_total = custo_compra + custo_estoque
            
            memo[quantidade] = custo_total
            return custo_total
        
        quantidades = [50, 100, 250, 500, 750, 1000, 1500]
        print("\nAnálise de custos por quantidade:")
        
        melhor_qtd = None
        melhor_custo = float('inf')
        
        for qtd in quantidades:
            custo = calcular_custo_otimo(qtd)
            print(f"  Quantidade: {qtd:4d} | Custo Total: R$ {custo:,.2f}")
            
            if custo < melhor_custo:
                melhor_custo = custo
                melhor_qtd = qtd
        
        print(f"\n✓ Quantidade ótima: {melhor_qtd} unidades")
        print(f"✓ Custo mínimo: R$ {melhor_custo:,.2f}")

    def executar_demonstracao_completa(self):
        """Executa demonstração completa do sistema"""
        print("\n" + "="*80)
        print("SISTEMA DE GESTÃO DE ESTOQUE DASA - DEMONSTRAÇÃO COMPLETA")
        print("="*80)
        
        self.demonstrar_sistema()
        
        self.demonstrar_estruturas_dados()
        
        self.demonstrar_algoritmos()
        
        self._gerar_relatorio_performance()
        
        print("\n" + "="*80)
        print("DEMONSTRAÇÃO CONCLUÍDA COM SUCESSO!")
        print("="*80)
    
    def _gerar_relatorio_performance(self):
        """Gera relatório de performance do sistema"""
        print("\n" + "="*60)
        print("RELATÓRIO DE PERFORMANCE")
        print("="*60)
        
        
        print("\nTempo de execução para operações principais:")
        
        start = time.time()
        for i in range(1000):
            self.sistema.registrar_consumo(
                f"UN{i%5+1}", 
                f"Material{i%20+1}", 
                random.randint(1, 10)
            )
        tempo_insercao = time.time() - start
        print(f"  • Inserção de 1000 registros: {tempo_insercao:.3f}s")
        
        
        start = time.time()
        for _ in range(100):
            materiais = list(self.sistema.estoque["UN1"].keys()) 
            if materiais:
                self.sistema.consultar_estoque("UN1", random.choice(materiais))
        tempo_busca = time.time() - start
        print(f"  • 100 consultas de estoque: {tempo_busca:.3f}s")
        
        start = time.time()
        self.analisador.analisar_padroes_consumo()
        tempo_analise = time.time() - start
        print(f"  • Análise de padrões: {tempo_analise:.3f}s")
        
        start = time.time()
        self.analisador.otimizar_distribuicao_entre_unidades()
        tempo_otimizacao = time.time() - start
        print(f"  • Otimização de distribuição: {tempo_otimizacao:.3f}s")
        
        print("\nEstatísticas do sistema:")
        total_registros = sum(len(h) for h in self.sistema.historico_consumo.values()) 
        total_materiais = sum(len(e) for e in self.sistema.estoque.values()) 
        
        print(f"  • Total de registros de consumo: {total_registros}")
        print(f"  • Total de materiais em estoque: {total_materiais}")
        print(f"  • Memória aproximada utilizada: {self._calcular_memoria_utilizada()} MB")
    
    def _calcular_memoria_utilizada(self):
        """Calcula memória aproximada utilizada pelo sistema"""
        
        total_size = 0
        total_size += sys.getsizeof(self.sistema.estoque)
        total_size += sys.getsizeof(self.sistema.historico_consumo)
        total_size += sys.getsizeof(self.sistema.alertas)
        
        return round(total_size / (1024 * 1024), 2) 