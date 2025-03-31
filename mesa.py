from datetime import datetime

class Mesa:
    def __init__(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade
        self.reservas = []  # Lista de reservas (data_hora, numero_pessoas)

    # Função para reservar mesa
    def reservar(self, data_hora, numero_pessoas):
        if self.esta_disponivel(data_hora, numero_pessoas):
            self.reservas.append((data_hora, numero_pessoas))
            return True
        return False

    # Função para verificar se a mesa está disponível
    def esta_disponivel(self, data_hora, numero_pessoas):
        if numero_pessoas > self.capacidade:
            return False  # Mesa não tem capacidade suficiente
        for reserva in self.reservas:
            if reserva[0] == data_hora:
                return False  # Já existe uma reserva no mesmo horário
        return True