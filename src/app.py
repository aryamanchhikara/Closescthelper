import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title('Boiler plate for the color check website')

st.subheader('Insert the image you want to perform color analysis on ')

uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Convert the file to an OpenCV image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    # Display the image using Streamlit
    st.image(image, channels="BGR", caption="Uploaded Image")
else:
    st.write("No file selected.")