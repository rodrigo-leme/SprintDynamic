from business_logic.stock_management import SistemaGestaoEstoque
import random

class AnalisadorDados:
    """
    realiza análises preditivas, identifica padrões de consumo e otimiza
    a distribuição de materiais entre as unidades.
    """
    def __init__(self, sistema_gestao_estoque: SistemaGestaoEstoque):
        self.sistema = sistema_gestao_estoque

    def analisar_padroes_consumo(self):
        """analisa o histórico de consumo para identificar padrões."""
        print("\nAnálise de Padrões de Consumo:")
        padroes = {}
        for unidade, historico in self.sistema.historico_consumo.items():
            for registro in historico:
                material = registro["material"]
                quantidade = registro["quantidade"]
                
                if material not in padroes:
                    padroes[material] = {"total_consumido": 0, "num_consumos": 0}
                
                padroes[material]["total_consumido"] += quantidade
                padroes[material]["num_consumos"] += 1
        
        if not padroes:
            print("  Não há dados de consumo para analisar.")
            return {}

        for material, dados in padroes.items():
            avg_consumo = dados["total_consumido"] / dados["num_consumos"]
            print(f"  - Material: {material} | Consumo Médio: {avg_consumo:.2f} unidades/registro")
        
        return padroes

    def prever_necessidades_futuras(self):
        """prevê necessidades futuras com base em padrões de consumo."""
        print("\nPrevisão de Necessidades Futuras:")
        previsoes = {}
        padroes = self.analisar_padroes_consumo() 
        if not padroes:
            print("  não é possível prever necessidades sem dados de consumo.")
            return {}
        
        
        for material, dados in padroes.items():
            avg_consumo = dados["total_consumido"] / dados["num_consumos"]
            previsao_proximo_mes = avg_consumo * 1.2 
            previsoes[material] = previsao_proximo_mes
            print(f"  - Material: {material} | Previsão Próximo Período: {previsao_proximo_mes:.2f} unidades")
            
        return previsoes

    def otimizar_distribuicao_entre_unidades(self):
        """melhora a distribuição de materiais entre unidades (simulação simples)."""
        print("\nOtimização de Distribuição entre Unidades:")
        transferencias_sugeridas = []
        
        
        estoque_total_por_material = {}
        estoque_por_unidade_material = {}

        for unidade, materiais in self.sistema.estoque.items():
            estoque_por_unidade_material[unidade] = {} 
            for material, qtd in materiais.items():
                estoque_total_por_material[material] = estoque_total_por_material.get(material, 0) + qtd
                estoque_por_unidade_material[unidade][material] = qtd
        
        if not estoque_total_por_material:
            print("  sem materiais em estoque para otimizar.")
            return []


        num_unidades = len(self.sistema.estoque)
        if num_unidades == 0:
            print("  sem unidades para otimizar a distribuição.")
            return []

        for material, total_qtd in estoque_total_por_material.items():
            ideal_por_unidade = total_qtd / num_unidades
            
            unidades_com_excesso = []
            unidades_com_falta = []

            for unidade in estoque_por_unidade_material.keys(): 
                qtd_na_unidade = estoque_por_unidade_material.get(unidade, {}).get(material, 0)
                if qtd_na_unidade > ideal_por_unidade * 1.1: 
                    excesso = qtd_na_unidade - ideal_por_unidade
                    unidades_com_excesso.append((unidade, excesso))
                elif qtd_na_unidade < ideal_por_unidade * 0.9:  
                    falta = ideal_por_unidade - qtd_na_unidade
                    unidades_com_falta.append((unidade, falta))
            
            for origem, exc_qtd in unidades_com_excesso:
                for destino, fal_qtd in unidades_com_falta:
                    qtd_transferir = min(exc_qtd, fal_qtd)
                    if qtd_transferir > 0:
                        transferencias_sugeridas.append({
                            "origem": origem,
                            "destino": destino,
                            "material": material,
                            "quantidade": round(qtd_transferir)
                        })
                        print(f"  →  transferência de {round(qtd_transferir)} de {material} de {origem} para {destino}")
                        exc_qtd -= qtd_transferir
                        fal_qtd -= qtd_transferir
                        
        if not transferencias_sugeridas:
            print("  nenhuma otimização de distribuição sugerida no momento.")

        return transferencias_sugeridas

    def transferir_entre_unidades(self, origem, destino, material, quantidade):
        """testa a transferência de material entre unidades."""
        if quantidade <= 0:
            print("Erro:  quantidade a transferir deve ser positiva.")
            return

        estoque_origem = self.sistema.consultar_estoque(origem, material)
        if estoque_origem is None or estoque_origem < quantidade:
            print(f"Erro: estoque insuficiente de {material} em {origem} para transferir {quantidade} unidades.")
            return
        
        self.sistema.data_store.update_estoque(origem, material, estoque_origem - quantidade)
        current_stock_destino = self.sistema.data_store.get_estoque(destino, material) or 0
        self.sistema.data_store.update_estoque(destino, material, current_stock_destino + quantidade)
        
        print(f"transferência de {quantidade} de {material} de {origem} para {destino} realizada com sucesso.")
        self.sistema._verificar_alerta_minimo(origem, material) 
        self.sistema._verificar_alerta_minimo(destino, material) 