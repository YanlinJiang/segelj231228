import streamlit as st2
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image

#st.title = ("# 绘图展示页面")
st2.header("""这是绘图展示页面""")
st2.subheader("""测试一下单项选择按钮：""")
selectButton = st2.radio(
    "选择您的图片处理场景:",
    ('自然','人物','黑夜')
)
if selectButton=='自然':
    st2.write("选了自然")
elif selectButton=='人物':
    st2.write("选了人物")
elif selectButton=='黑夜':
    st2.write("选了黑夜")
