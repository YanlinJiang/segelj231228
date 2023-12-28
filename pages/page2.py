import streamlit as st2
from PIL import Image
import io
#st.title = ("# 绘图展示页面")
st2.header("""这是上传图片展示页面""")
st2.title("Upload Image")
image_file = st2.file_uploader("Upload Images",
type=["png","jpg","jpeg"])
check_details = st2.button("Check Details")
if check_details:
    if image_file is not None:
            # To See details
            image_details = {"file_name":image_file.name,
            "file_type":image_file.type,
            "file_size":image_file.size}
            st2.write(image_details)
            # To View Uploaded Image
            image_data = image_file.read()
            image = Image.open(io.BytesIO(image_data))
            st2.image(image, width=250)


    else:
        st2.write("No Image File is Uploaded")
