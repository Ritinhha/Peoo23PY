#import streamlit as st
#st.header ("POO em Python com streamlit")
#if st.button ("Clique aqui"):
    #st.write ("Bem vindo ao streamlit")

from templantes.manterclienteUI import ManterClienteUI
from templantes.manterservicoUI import ManterServicoUI
from templantes.manteragendaUI import ManterAgendaUI
from templantes.abriragendaUI import AbrirAgendaUI

import streamlit as st

class IndexUI:

    def sidebar():
      op = st.sidebar.selectbox("Menu", ["Manter Clientes", "Manter Serviços", "Manter Agenda", "Abrir Agenda do Dia"])
      if op == "Manter Clientes": ManterClienteUI.main()
      if op == "Manter Serviços": ManterServicoUI.main()
      if op == "Manter Agenda": ManterAgendaUI.main()
      if op == "Abrir Agenda do Dia": AbrirAgendaUI.main()

      
    def main():
      IndexUI.sidebar()

IndexUI.main()