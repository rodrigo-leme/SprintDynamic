class StockData:
    """
    gerencia o armazenamento de dados de estoque e histórico de consumo.
    """
    def __init__(self):
        self.estoque = {}  
        self.historico_consumo = {}  
        self.alertas = {}  

    def get_estoque(self, unidade, material=None):
        """retorna o estoque de um material específico ou de toda a unidade."""
        if unidade not in self.estoque:
            return None if material else {}
        if material:
            return self.estoque[unidade].get(material)
        return self.estoque[unidade]

    def update_estoque(self, unidade, material, quantidade):
        """atualiza a quantidade de um material no estoque."""
        if unidade not in self.estoque:
            self.estoque[unidade] = {}
        self.estoque[unidade][material] = quantidade

    def add_historico_consumo(self, unidade, material, quantidade, timestamp):
        """adiciona um registro ao histórico de consumo."""
        if unidade not in self.historico_consumo:
            self.historico_consumo[unidade] = []
        self.historico_consumo[unidade].append({
            "material": material,
            "quantidade": quantidade,
            "timestamp": timestamp
        })

    def get_historico_consumo(self, unidade):
        """retorna o histórico de consumo de uma unidade."""
        return self.historico_consumo.get(unidade, [])

    def set_limite_minimo(self, unidade, material, limite):
        """ddefine o limite mínimo para um material em uma unidade."""
        if unidade not in self.alertas:
            self.alertas[unidade] = {}
        self.alertas[unidade][material] = limite

    def get_limite_minimo(self, unidade, material):
        """retorna o limite minimo de um material."""
        return self.alertas.get(unidade, {}).get(material) 