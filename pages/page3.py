# Import following libraries
import streamlit as st3
from PIL import Image
import os
import io
# Defining File Upload Method of Streamlit
st3.title("Saving File to Directory")
image_file = st3.file_uploader("Upload Images",
            type=["png","jpg","jpeg"])
# Defining path where file to be saved
file_save_path = "saveData"
save_file = st3.button("Check Details & Save")
if save_file:
    if image_file is not None:
            # To See details
            image_details = {"file_name":image_file.name,
            "file_type":image_file.type,
                            "file_size":image_file.size}
            st3.write(image_details)
            # To View Uploaded Image
            image_data = image_file.read()
            image = Image.open(io.BytesIO(image_data))
            st3.image(image, width=250)
            with open(os.path.join(file_save_path,image_file.name),"wb") as f:
                f.write((image_file).getbuffer())
            st3.success("Image Saved Successfully")
    else:
            st3.write("No Image File is Uploaded")