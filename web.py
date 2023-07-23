import streamlit as st
# PIL is a package with Image type
from PIL import Image

# we need a subheader
st.subheader("Color To Grayscale Converter")

# The user is also given an option to upload an image
uploaded_image = st.file_uploader("Upload an image")

# we need a camera input
with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")

# camera_image is an Uploader File object
# we need an Image object in order to perform the grayscale operation
# Another thing to be noted is that initially until we allow the camera:
# The value of camera_image is None

if camera_image:
    # creating an Image instance from the Camera input
    PIL_Image = Image.open(camera_image)
    # applying grayscale
    grayscale_image = PIL_Image.convert("L")
    # displaying gray-scaled image
    st.image(grayscale_image)
if uploaded_image:
    # creating an Image instance from the Camera input
    PIL_Image = Image.open(uploaded_image)
    # applying grayscale
    grayscale_image = PIL_Image.convert("L")
    # displaying gray-scaled image
    st.image(grayscale_image)





