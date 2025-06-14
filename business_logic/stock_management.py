from data_layer.storage import StockData
import datetime

class SistemaGestaoEstoque:
    """
    gerencia as operações de estoque, como registro de consumo, reabastecimento,
    consultas e alertas de nível mínimo.
    """
    def __init__(self):
        self.data_store = StockData()
        self.estoque = self.data_store.estoque  # Referência direta para simplificar a demonstração
        self.historico_consumo = self.data_store.historico_consumo
        self.alertas = self.data_store.alertas

    def registrar_consumo(self, unidade, material, quantidade):
        """registra o consumo de um material em uma unidade."""
        if quantidade <= 0:
            print("Erro: A quantidade de consumo deve ser positiva.")
            return
        
        current_stock = self.data_store.get_estoque(unidade, material) or 0
        new_stock = current_stock - quantidade
        
        if new_stock < 0:
            print(f"Alerta: Consumo de {quantidade} unidades de {material} na {unidade} excede o estoque disponível ({current_stock}).")
            # return
            
        self.data_store.update_estoque(unidade, material, max(0, new_stock))
        self.data_store.add_historico_consumo(unidade, material, quantidade, datetime.datetime.now())
        self._verificar_alerta_minimo(unidade, material)
        print(f"Consumo registrado: {quantidade} unidades de {material} na {unidade}. Estoque atual: {max(0, new_stock)}.")

    def reabastecer(self, unidade, material, quantidade):
        """registra o reabastecimento de um material em uma unidade."""
        if quantidade <= 0:
            print("Erro: A quantidade de reabastecimento deve ser positiva.")
            return
        
        current_stock = self.data_store.get_estoque(unidade, material) or 0
        new_stock = current_stock + quantidade
        self.data_store.update_estoque(unidade, material, new_stock)
        print(f"reabastecimento registrado: {quantidade} unidades de {material} na {unidade}. Estoque atual: {new_stock}.")

    def consultar_estoque(self, unidade, material=None):
        """consultaa o estoque de um material específico ou de toda a unidade."""
        if material:
            quantidade = self.data_store.get_estoque(unidade, material)
            if quantidade is not None:
                print(f"estoque de {material} na {unidade}: {quantidade} unidades.")
                return quantidade
            else:
                print(f"Material '{material}' não encontrado na unidade '{unidade}'.")
                return None
        else:
            estoque_unidade = self.data_store.get_estoque(unidade)
            if estoque_unidade:
                print(f"Estoque da unidade {unidade}:")
                for mat, qtd in estoque_unidade.items():
                    print(f"  - {mat}: {qtd} unidades")
                return estoque_unidade
            else:
                print(f"Unidade '{unidade}' sem materiais registrados ou não encontrada.")
                return {}

    def definir_limite_minimo(self, unidade, material, limite):
        """define um limite mínimo de estoque para um material."""
        if limite < 0:
            print("Erro: O limite mínimo não pode ser negativo.")
            return
        self.data_store.set_limite_minimo(unidade, material, limite)
        print(f"Limite mínimo de {limite} para {material} na {unidade} definido.")
        self._verificar_alerta_minimo(unidade, material)

    def verificar_alertas(self):
        """verifica e retorna os materiais abaixo do limite mínimo."""
        alertas_atuais = []
        for unidade, materiais_alertas in self.data_store.alertas.items():
            for material, limite in materiais_alertas.items():
                current_stock = self.data_store.get_estoque(unidade, material) or 0
                if current_stock < limite:
                    alertas_atuais.append({
                        "unidade": unidade,
                        "material": material,
                        "estoque_atual": current_stock,
                        "limite_minimo": limite
                    })
        if alertas_atuais:
            print("\nALERTA: Materiais abaixo do limite mínimo!")
            for alerta in alertas_atuais:
                print(f"""  - Unidade: {alerta['unidade']}, Material: {alerta['material']},
                   Estoque: {alerta['estoque_atual']}, Limite: {alerta['limite_minimo']}""")
        else:
            print("\nSem alertas de estoque no momento.")
        return alertas_atuais

    def _verificar_alerta_minimo(self, unidade, material):
        """verifica se um material está abaixo do limite mínimo e exibe um alerta."""
        limite = self.data_store.get_limite_minimo(unidade, material)
        if limite is not None:
            current_stock = self.data_store.get_estoque(unidade, material) or 0
            if current_stock < limite:
                print(f"*** ALERTA: {material} na {unidade} está abaixo do limite mínimo ({current_stock}/{limite}) ***") 