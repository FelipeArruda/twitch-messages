# from flask import Flask
# import os
import streamlit as st

# app = Flask(__name__)



# @app.route("/")
# def hello_world():
#     return "AWS 25"
def main():
    page = st.sidebar.selectbox("Escolha uma opção:", ['Opção 1', 'Opção 2', 'Opção 3'])
    st.header("Twicth - Análise de dados")
    st.write('Esta é uma página de teste.')

if __name__ == "__main__":
    main()
    # port = int(os.environ.get("PORT", 5000))
    # app.run(host='0.0.0.0', port=port)