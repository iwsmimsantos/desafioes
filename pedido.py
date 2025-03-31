class Pedido:
    def __init__(self, prato, quantidade):
        self.prato = prato
        self.quantidade = quantidade
        self.status = "Em andamento"

    def calcular_total(self):
        return self.prato.preco * self.quantidade
