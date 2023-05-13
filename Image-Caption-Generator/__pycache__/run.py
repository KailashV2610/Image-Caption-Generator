import streamlit as st
from main import predict_step
from PIL import Image

st.title("Image Processing App")
st.write("Select an image file from your computer:")

# File uploader
uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Open and display the image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    # Process the image
    processed_text = predict_step([uploaded_file])
    st.write("Caption:")
    st.write(processed_text)
