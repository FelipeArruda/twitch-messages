import pandas as pd
import streamlit as st
from src.Mysql import MysqlDriver
st.set_page_config("Twitch - Análise de dados")


def main():
    conn_mysql = MysqlDriver(None)
    # page = st.sidebar.selectbox("Escolha uma opção:", ['Opção 1', 'Opção 2', 'Opção 3'])
    st.markdown("### Data preview")
    data = conn_mysql.query("select channel, count(*) from twitch.event_message group by channel order by 2 desc")
    df = pd.DataFrame(
        data,
        columns=(['Canal', 'Mensagens'])
    )
    st.dataframe(df)


if __name__ == "__main__":
    main()
