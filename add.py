import streamlit as st
from src.extraction import load_data

st.set_page_config(layout = 'wide')

def create_dataframe_section(df):
    st.title('Database Section')
    col1, col2 = st.columns(2)
def create_answer_sections(df):
    st.title('Sessão de respostas')

def main():
    df_raw = load_data()
    create_dataframe_section(df_raw)
    st.dataframe(df_raw)
    



if __name__ == '__main__':
    main()
