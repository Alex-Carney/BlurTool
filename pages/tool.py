import streamlit as st
from PIL import Image
import numpy as np
import plotly.express as px
from streamlit_plotly_events import plotly_events
from common.components_callbacks import register_callback

def app():
    def load_image(image_file):
        img = Image.open(image_file)
        return img

    def upload_image_callback():
        print(st.session_state.uploaded_img)
        if st.session_state.uploaded_img is not None:
            print("INSIDE UPLOAD IMAGE")
            image = Image.open(st.session_state.uploaded_img)
            render_image(image)

    def render_image(image):
        print("RENDERING IMAGE")
        st.session_state.curr_image = image
        fig = px.imshow(image)
        if st.session_state.just_uploaded:
            st.session_state.just_uploaded = False
            with col2:
                plotly_events(fig, key="my_key")


    def click_image_callback():
        print("INSIDE CLICK IMAGE CALLBACK")
        print("You clicked " + str(st.session_state.my_key))

        # Get the current image. Do something to it, then pass it on to render_image

        render_image(st.session_state.curr_image)


# --------------------------------- WIDGETS



    st.subheader("Image")

    col1, col2 = st.columns([1, 3])
    st.session_state.col2 = col2

    st.session_state.just_uploaded = True

    register_callback("my_key", click_image_callback)

    col1.file_uploader("Upload Images", type=["png", "jpg", "jpeg"], key="uploaded_img", on_change=upload_image_callback)

    # register_callback("my_key", click_image_callback)

    # if image_file is not None:
    #
    #     print("I AM IN SIDE OF HERE RIGHT NOW")
    #
    #
    #     image = Image.open(image_file)
    #
    #     # To See details
    #     file_details = {"filename": image_file.name, "filetype": image_file.type,
    #               "filesize": image_file.size}
    #     # st.write(file_details)
    #
    #     # To View Uploaded Image
    #     fig = px.imshow(image)
    #     st.session_state.clicked_points = plotly_events(fig, key="uploaded_image")
    #
    #     converted_img = np.array(image.convert('RGB'))
    #
    #     register_callback("uploaded_image", click_image_callback)




        # print(converted_img)
        # print(np.shape(converted_img))
        #
        # st.image(converted_img, channels='GRB')