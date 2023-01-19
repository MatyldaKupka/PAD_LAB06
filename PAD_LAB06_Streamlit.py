import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.DataFrame(px.data.gapminder())

def Ankieta():
    firstname = st.text_input("Please, enter your 1st name", "Type here...")
    if st.button("Submit first name"):
        result = firstname.title()
        st.success(result)
    secondname = st.text_input("Please enter your second name", "Type here...")
    if st.button("Submit second name"):
        result1 = secondname.title()
        st.success(result1)
    

def Staty():
    data = st.file_uploader("Upload your dataset", type=['csv'])
    


    if data is not None:
        import time
        my_bar = st.progress(0)
        for p in range(100):
            time.sleep(0.1)
            my_bar.progress(p + 1)

        df = pd.read_csv(data)
        st.dataframe(df.head(10))
        st.set_option('deprecation.showPyplotGlobalUse', False)
        all_columns_names = df.columns.to_list()
        selected_column_names = st.multiselect("Select columns to plot", all_columns_names)
        
        plot_data = df[selected_column_names]
        st.bar_chart(plot_data)
        st.line_chart(plot_data)

    


page = st.sidebar.selectbox('Select page',['Ankieta','Staty']) 
if page == 'Ankieta':
    Ankieta()
else:
    Staty()