import streamlit as st
import pandas as pd
from views import View
import time
from datetime import datetime, timedelta


class VizualizarMeusAgendamentosUI:
  def main():
    st.header("Meus Agendamentos")
    VizualizarMeusAgendamentosUI.listar()

# Função para gerar horários para uma semana
def gerar_horarios_semana(data_inicial, dias_na_semana=7, intervalo_de_tempo=timedelta(hours=1)):
    horarios_semana = {}
    for dia in range(dias_na_semana):
        horarios_dia = []
        horario_atual = datetime(data_inicial.year, data_inicial.month, data_inicial.day, 9, 0, 0)  # Inicia às 9:00
        for _ in range(8):  # 8 horas de atendimento diário
            horarios_dia.append(horario_atual)
            horario_atual += intervalo_de_tempo
        horarios_semana[data_inicial.strftime('%Y-%m-%d')] = horarios_dia
        data_inicial += timedelta(days=1)
    return horarios_semana

# Função para exibir horários disponíveis
def exibir_horarios_disponiveis(horarios_semana):
    for data, horarios_dia in horarios_semana.items():
        print(f"Horários disponíveis para {data}:")
        for horario in horarios_dia:
            print(horario.strftime('%H:%M'))
        print()

# Função para agendar um horário
def agendar_horario(horarios_semana, agendamentos, cliente, data, hora):
    try:
        horario_selecionado = datetime.strptime(f"{data} {hora}", '%Y-%m-%d %H:%M')
        if horario_selecionado in horarios_semana[data]:
            agendamentos.append({
                'cliente': cliente,
                'data': data,
                'hora': hora
            })
            print(f"Horário {hora} agendado com sucesso para o dia {data}.")
        else:
            print("Horário indisponível. Escolha outro horário.")
    except ValueError:
        print("Formato de data ou hora inválido.")

# Função para visualizar os agendamentos de um cliente em um período
def visualizar_agendamentos(agendamentos, cliente, data_inicial, data_final):
    print(f"Agendamentos para o cliente {cliente} no período de {data_inicial} a {data_final}:")
    for agendamento in agendamentos:
        if data_inicial <= agendamento['data'] <= data_final and agendamento['cliente'] == cliente:
            print(f"{agendamento['data']} às {agendamento['hora']}")
    print()

# Defina a data inicial como hoje
data_inicial = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

# Gere os horários da semana
horarios_semana = gerar_horarios_semana(data_inicial)

# Lista para armazenar os agendamentos
agendamentos = []

# Exiba os horários disponíveis
exibir_horarios_disponiveis(horarios_semana)

# Exemplo de agendamento
cliente = "João"
data_agendamento = input("Digite a data do agendamento (formato YYYY-MM-DD): ")
hora_agendamento = input("Digite a hora do agendamento (formato HH:MM): ")

agendar_horario(horarios_semana, agendamentos, cliente, data_agendamento, hora_agendamento)

# Exemplo de visualização de agendamentos
data_inicial_visualizacao = input("Digite a data inicial para visualizar os agendamentos (formato YYYY-MM-DD): ")
data_final_visualizacao = input("Digite a data final para visualizar os agendamentos (formato YYYY-MM-DD): ")

visualizar_agendamentos(agendamentos, cliente, data_inicial_visualizacao, data_final_visualizacao)
