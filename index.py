import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image

st.header("""This is Header""")
st.subheader("""This is subHeader""")
st.caption("""This is caption""")
st.write("Hello")
st.text("Hi!\nthe enter is input\tqwq")
st.markdown("# Hi, \n # ***test markdown*** \t !!!!!!")
st.markdown("###### smaller size character test")
st.latex(r'''\beta \sum^{\Omega }_{\lambda =1} sin^{2}\times \frac{\sqrt[2]{\pi \otimes \chi } }{\Delta \delta } ''')

st.subheader("""code presentation:""")
code = '''def hello():
print("Hello world!")'''
st.code(code, language='python')

# 测试一下表格:
df = pd.DataFrame(
    np.random.randn(5,10),
    columns = ('未命名列_%d' % i for i in range(10))
)
df.index = ['未命名行_%d' % i for i in range(5)]
#动态表格
st.subheader("""动态表格测试：""")
st.dataframe(df.style.highlight_min())
#静态表格
st.subheader("""静态表格测试：""")
st.table(df)


#测试一下chart
df_c = pd.DataFrame(
    np.random.randn(10,2),
    columns = ['a','b']
)
chart = alt.Chart(df_c).mark_bar().encode(
    x='a', y='b', tooltip=['a', 'b']
)
st.write(chart)


#放个本地图
st.write("放张本地图片测试")
referImage = Image.open("images/testImage.jpg")
#referImage = referImage.resize((400, 200))
st.image(referImage,width=400)

st.subheader("下载上面的图：")
# Creating Download Button
down_btn = st.download_button(
        label="下载！",
        data=open("images/testImage.jpg", "rb"),
        file_name="picture.jpg",
        mime="image/jpg"
)

st.write("放多张本地图片测试")
listImages=[
    referImage,
    referImage,
    referImage
]
st.image(listImages,width=150)

#放入测试视频：
#referVideo = open("images/testVideo.mp4", "rb").read()
#st.video(referVideo, start_time = 10,width=200)

#放入一个按钮
buttonT1 = st.button("一个按钮")
if buttonT1:
    referVideo = open("images/testVideo.mp4", "rb").read()
    st.video(referVideo, start_time = 10)
else:
    st.write("还没点按钮")

#放入一个单选按钮
st.subheader("""测试一下单项选择按钮：""")
selectButton = st.radio(
    "选择您的图片处理场景:",
    ('自然','人物','黑夜')
)
if selectButton=='自然':
    st.write("选了自然")
elif selectButton=='人物':
    st.write("选了人物")
elif selectButton=='黑夜':
    st.write("选了黑夜")

st.subheader("""测试一下拉窗按钮：""")
boxButton = st.selectbox('选择一个算法:',
             ('A算法','B算法','C算法','请点击选择'),index=3)
if boxButton=='A算法':
    st.write("AAAAAAAAA")
elif boxButton=='B算法':
    st.write("BBBBBBBBB")
elif boxButton=='C算法':
    st.write("CCCCCCCCC")


Algorithm = st.multiselect(
      '选择多个算法:',
      ['A算法', 'B算法', 'C算法',
      'D算法', 'E算法', 'F算法'])









