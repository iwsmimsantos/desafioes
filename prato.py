class Prato:
    def __init__(self, nome, tipo, preco, descricao):
        self.nome = nome
        self.tipo = tipo
        self.preco = preco
        self.descricao = descricao

    def exibir_info(self):
        print(f"Nome: {self.nome}, Tipo: {self.tipo}, Preço: R${self.preco:.2f}, Descrição: {self.descricao}")
