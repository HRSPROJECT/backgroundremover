import streamlit as st
from rembg import remove
from PIL import Image
import io
import webbrowser

st.title("Background Remover")

with st.sidebar:
  if st.button("Explore More"):
      webbrowser.open_new_tab("https://hrsproject.github.io/home/")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    try:
        input_image = Image.open(uploaded_file)
        output_image = remove(input_image,
                             alpha_matting=True,
                             alpha_matting_foreground_threshold=250,
                             alpha_matting_background_threshold=10,
                             session=None
                             )

        # Save the image into in-memory bytes object
        output_image_bytes = io.BytesIO()
        output_image.save(output_image_bytes, format="PNG")
        output_image_bytes.seek(0)

        st.image(output_image, caption="Processed Image", use_column_width=True)

        st.download_button(
            label="Download Processed Image",
            data=output_image_bytes,
            file_name="output_image.png",
            mime="image/png",
        )
    except Exception as e:
        st.error(f"An error occurred: {e}")
