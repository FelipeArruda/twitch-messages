import streamlit as st

st.set_page_config("Twitch - Análise de dados")

def main():

    page = st.sidebar.selectbox("Escolha uma opção:", ['Opção 1', 'Opção 2', 'Opção 3'])
    st.header("Twitch - Análise de dadosss")
    st.write('Esta é uma página de teste.')

if __name__ == "__main__":
    main()
