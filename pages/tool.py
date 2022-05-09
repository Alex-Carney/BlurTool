import streamlit as st
from PIL import Image
import numpy as np
import plotly.express as px
from streamlit_plotly_events import plotly_events
from common.components_callbacks import register_callback
import common.convolution as conv
import json

kernels = {
    "Gauss Blur 3x3": np.array([[1 / 16, 2 / 16, 1 / 16], [2 / 16, 4 / 16, 2 / 16], [1 / 16, 2 / 16, 1 / 16]]),
    "Gauss Blur 5x5": (1/256) * np.array([[1, 4, 6, 4, 1], [4, 16, 24, 16, 4], [6, 24, 36, 24, 6], [4, 16, 24, 16, 4], [1, 4, 6, 4, 1]]),
    "Box Blur": (1/9) * np.ones((3, 3)),
    "Bruh": np.array([[0, 1, 0], [1, 5, 1], [0, 1, 0]]),
    "????": np.random.rand(3, 3)
}



def app():

    def upload_image_callback():
        print(st.session_state.uploaded_img)
        if st.session_state.uploaded_img is not None:
            image = Image.open(st.session_state.uploaded_img)
            render_image(image)

    def render_image(image):
        st.session_state.curr_image = image
        fig = px.imshow(image)
        if st.session_state.just_uploaded:
            st.session_state.just_uploaded = False
            plotly_events(fig, key="my_key")

    def option_change_callback():
        if 'curr_image' in st.session_state:
            render_image(st.session_state.curr_image)


    def click_image_callback():

        # Get the current image. Do something to it, then pass it on to render_image
        str_without_brack = st.session_state.my_key[1:-1]
        result = json.loads(str_without_brack)
        print(result)
        st.session_state.curr_image = conv.convolution_2(st.session_state.curr_image,
                                                         kernels[st.session_state.kernel],
                                                         result['pointIndex'],
                                                         st.session_state.blur_radius)

        render_image(st.session_state.curr_image)

    def blur_full_image_callback():
        try:
            st.session_state.curr_image = conv.convolution(st.session_state.curr_image,
                                                           kernels[st.session_state.kernel])
            render_image(st.session_state.curr_image)
        except:
            st.warning("Can't do this right now. Upload an image first")


# --------------------------------- WIDGETS



    st.subheader("Image")

    col1, col2 = st.columns([1, 3])
    st.session_state.col2 = col2

    st.session_state.just_uploaded = True

    register_callback("my_key", click_image_callback)

    st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"], key="uploaded_img", on_change=upload_image_callback)

    col1.button("Reset Image", key="reset", on_click=upload_image_callback)

    col1.button("Full Image", on_click=blur_full_image_callback)

    col2.slider("Blur Radius", key="blur_radius", min_value=5, max_value=500, value=50, step=1, on_change=option_change_callback)

    col2.selectbox("Kernel", ["Gauss Blur 3x3", "Gauss Blur 5x5", "Box Blur", "Bruh", "????"], key='kernel', on_change=option_change_callback)