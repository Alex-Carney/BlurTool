import streamlit as st
from PIL import Image
import numpy as np

def app():
    def load_image(image_file):
        img = Image.open(image_file)
        return img


    st.subheader("Image")
    image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])

    if image_file is not None:


        image = Image.open(image_file)

        # To See details
        file_details = {"filename": image_file.name, "filetype": image_file.type,
                  "filesize": image_file.size}
        st.write(file_details)

        # To View Uploaded Image
        st.image(image, width=500)

        converted_img = np.array(image.convert('RGB'))

        print(converted_img)
        print(np.shape(converted_img))

        st.image(converted_img, channels='GRB')