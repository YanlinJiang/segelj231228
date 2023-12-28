import streamlit as st1
import pandas as pd
import numpy as np
import plotly.express as px

#st.title = ("# 绘图展示页面")
st1.header("""这是绘图展示页面""")
col1, padding, col2 = st1.columns((10,2,10))
with col1:
    st1.title('Area')
    # Defining dataframe with its values
    df = pd.DataFrame(
        np.random.randn(40, 4),
        columns=["C1", "C2", "C3", "C4"])
    # Bar Chart
    st1.bar_chart(df)



with col2:
    st1.title('Area')
    # Defining dataframe with its values
    df = pd.DataFrame(
        np.random.randn(40, 4),
        columns=["C1", "C2", "C3", "C4"])
    # Bar Chart
    st1.area_chart(df)

    st1.title('Area')
    # Defining dataframe with its values
    df = pd.DataFrame(
        np.random.randn(40, 4),
        columns=["C1", "C2", "C3", "C4"])
    # Bar Chart
    st1.line_chart(df)
