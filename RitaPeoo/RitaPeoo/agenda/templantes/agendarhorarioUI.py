import streamlit as st
import pandas as pd
from views import View
from datetime import datetime, timedelta

class AgendarHorarioUI:
  def main():
    st.header("Agenda de Hoje")
    AgendarHorarioUI.listar()

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
def agendar_horario(horarios_semana, data, hora):
    try:
        horario_selecionado = datetime.strptime(f"{data} {hora}", '%Y-%m-%d %H:%M')
        if horario_selecionado in horarios_semana[data]:
            print(f"Horário {hora} agendado com sucesso para o dia {data}.")
            # Adicione lógica adicional, como a marcação do horário como ocupado, em um sistema mais complexo.
        else:
            print("Horário indisponível. Escolha outro horário.")
    except ValueError:
        print("Formato de data ou hora inválido.")

# Defina a data inicial como hoje
data_inicial = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

# Gere os horários da semana
horarios_semana = gerar_horarios_semana(data_inicial)

# Exiba os horários disponíveis
exibir_horarios_disponiveis(horarios_semana)

# Exemplo de agendamento
data_agendamento = input("Digite a data do agendamento (formato YYYY-MM-DD): ")
hora_agendamento = input("Digite a hora do agendamento (formato HH:MM): ")

agendar_horario(horarios_semana, data_agendamento, hora_agendamento)
