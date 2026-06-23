import streamlit as st
from yo import detect_objects

st.set_page_config(layout="wide")

st.title("YOLO Object Detection App")

# Upload image
uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Save uploaded image into data folder
    image_path = "data/samples.jpg"

    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image(image_path, caption="Uploaded Image")

    # Detect button
    if st.button("Run YOLO Detection"):

        output_path = detect_objects(image_path)

        st.success("Detection Complete!")

        st.image(output_path, caption="Detected Image")