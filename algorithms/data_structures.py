import heapq
from collections import defaultdict

# --- árvore  ---
class NoAVL:
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL:
 
    def _altura(self, no):
        if not no:
            return 0
        return no.altura

    def _atualizar_altura(self, no):
        if no:
            no.altura = 1 + max(self._altura(no.esquerda), self._altura(no.direita))

    def _get_balance(self, no):
        if not no:
            return 0
        return self._altura(no.esquerda) - self._altura(no.direita)

    def _rotacao_direita(self, y):
        x = y.esquerda
        T2 = x.direita

        x.direita = y
        y.esquerda = T2

        self._atualizar_altura(y)
        self._atualizar_altura(x)

        return x

    def _rotacao_esquerda(self, x):
        y = x.direita
        T2 = y.esquerda

        y.esquerda = x
        x.direita = T2

        self._atualizar_altura(x)
        self._atualizar_altura(y)

        return y

    def inserir(self, chave, valor):
        """Insere um novo nó na árvore AVL."""
        self.raiz = self._inserir(self.raiz, chave, valor)

    def _inserir(self, no, chave, valor):
        if not no:
            return NoAVL(chave, valor)

        if chave < no.chave:
            no.esquerda = self._inserir(no.esquerda, chave, valor)
        elif chave > no.chave:
            no.direita = self._inserir(no.direita, chave, valor)
        else:
            no.valor = valor 
            return no

        self._atualizar_altura(no)

        balance = self._get_balance(no)


        if balance > 1 and chave < no.esquerda.chave:
            return self._rotacao_direita(no)

        if balance < -1 and chave > no.direita.chave:
            return self._rotacao_esquerda(no)

        if balance > 1 and chave > no.esquerda.chave:
            no.esquerda = self._rotacao_esquerda(no.esquerda)
            return self._rotacao_direita(no)

        if balance < -1 and chave < no.direita.chave:
            no.direita = self._rotacao_direita(no.direita)
            return self._rotacao_esquerda(no)

        return no

    def buscar(self, chave):
        """busca um nó na árvore AVL pela chave."""
        return self._buscar(self.raiz, chave)

    def _buscar(self, no, chave):
        if not no or no.chave == chave:
            return no

        if chave < no.chave:
            return self._buscar(no.esquerda, chave)
        return self._buscar(no.direita, chave)

    def travessia_em_ordem(self, no):
        """faz a travessia em-ordem na árvore (para depuração/visualização)."""
        if no:
            self.travessia_em_ordem(no.esquerda)
            print(f"  - {no.chave}: {no.valor}")
            self.travessia_em_ordem(no.direita)

    def __init__(self):
        self.raiz = None


class MinHeap:
 
    def __init__(self):
        self.heap = []
        self.tamanho = 0

    def inserir(self, prioridade, item):
        """insere um item no heap com uma dada prioridade."""
        # heapq 
        heapq.heappush(self.heap, (prioridade, item))
        self.tamanho += 1

    def extrair_minimo(self):
        """remove e retorna o item de maior prioridade (menor valor)."""
        if self.tamanho == 0:
            return None
        self.tamanho -= 1
        return heapq.heappop(self.heap)

    def esta_vazio(self):
        """verifica se o heap está vazio."""
        return self.tamanho == 0

class Grafo:

    def __init__(self):
        self.grafo = defaultdict(list) 
        self.vertices = set()

    def adicionar_vertice(self, vertice):
        """adiciona um vértice ao grafo."""
        self.vertices.add(vertice)

    def adicionar_aresta(self, u, v, peso=1):
        """adiciona uma aresta (direcional) entre u e v com um peso."""
        self.adicionar_vertice(u)
        self.adicionar_vertice(v)
        self.grafo[u].append((v, peso))
        self.grafo[v].append((u, peso)) 

    def bfs(self, inicio):
        """executa Busca em Largura (BFS) a partir de um vértice inicial."""
        visitados = set()
        fila = [inicio]
        visitados.add(inicio)
        ordem_visita = []

        while fila:
            vertice_atual = fila.pop(0)
            ordem_visita.append(vertice_atual)

            for vizinho, _ in self.grafo[vertice_atual]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)
        return ordem_visita

    def dfs(self, inicio, visitados=None):
        if visitados is None:
            visitados = set()
        
        ordem_visita = []

        def _dfs_recursivo(vertice):
            visitados.add(vertice)
            ordem_visita.append(vertice)
            for vizinho, _ in self.grafo[vertice]:
                if vizinho not in visitados:
                    _dfs_recursivo(vizinho)

        _dfs_recursivo(inicio)
        return ordem_visita

    def dijkstra(self, inicio):
        """implementa o algoritmo de Dijkstra para encontrar o caminho mais curto."""
        distancias = {vertice: float('inf') for vertice in self.vertices}
        distancias[inicio] = 0
        fila_prioridade = [(0, inicio)] # (distancia, vertice)

        while fila_prioridade:
            dist_atual, vertice_atual = heapq.heappop(fila_prioridade)

            if dist_atual > distancias[vertice_atual]:
                continue

            for vizinho, peso in self.grafo[vertice_atual]:
                distancia = dist_atual + peso
                if distancia < distancias[vizinho]:
                    distancias[vizinho] = distancia
                    heapq.heappush(fila_prioridade, (distancia, vizinho))
        
        return {k: v for k, v in distancias.items() if v != float('inf')} 