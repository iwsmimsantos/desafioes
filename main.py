from datetime import datetime
from mesa import Mesa

# Função para verificar a disponibilidade e realizar a reserva
def verificar_disponibilidade_e_reservar(mesas, data_hora, numero_pessoas):
    for mesa in mesas:
        if mesa.esta_disponivel(data_hora, numero_pessoas):
            mesa.reservar(data_hora, numero_pessoas)
            return mesa.numero  # Retorna o número da mesa que foi reservada
    return None  # Retorna None se não houver mesa disponível

# Dados do restaurante
mesa1 = Mesa(1, 4)  # Mesa 1 com capacidade para 4 pessoas
mesa2 = Mesa(2, 2)  # Mesa 2 com capacidade para 2 pessoas
mesa3 = Mesa(3, 6)  # Mesa 3 com capacidade para 6 pessoas
mesa4 = Mesa(4, 8)  # Mesa 4 com capacidade para 8 pessoas

# Reservas existentes
mesa2.reservas.append((datetime(2024, 10, 28, 20, 30), 2))  # Mesa 2 já reservada para 2 pessoas às 20:30
mesa1.reservas.append((datetime(2024, 10, 28, 19, 0), 4)) 

# Lista de mesas
mesas = [mesa1, mesa2, mesa3, mesa4]

# Dados da reserva
data_reserva = datetime(2024, 10, 28, 20, 30)  # Cliente quer reservar para 20:30
numero_pessoas = 5  # Cliente quer reservar para 5 pessoas

# Verificando a disponibilidade e fazendo a reserva
mesa_reservada = verificar_disponibilidade_e_reservar(mesas, data_reserva, numero_pessoas)

# Resultado da operação
if mesa_reservada:
    print(f"Reserva confirmada! Mesa {mesa_reservada} foi reservada para {numero_pessoas} pessoas às {data_reserva.strftime('%Y-%m-%d %H:%M')}.")
else:
    print("Não há mesas disponíveis para o horário solicitado.")
