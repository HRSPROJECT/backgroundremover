import streamlit as st
from rembg import remove
from PIL import Image
import io
import streamlit.components.v1 as components

def open_link_button(label, url):
    components.html(
        f"""
        <a href="{url}" target="_blank" style="display: inline-block; padding: 10px 15px; border-radius: 5px; text-decoration: none; background-color: #007bff; color: white; border: none; cursor: pointer;">{label}</a>
        """,
        height=40,
    )


st.markdown(
    """
    <style>
        .navbar {
            display: flex;
            justify-content: flex-end;
            background-color: #f0f0f0;
            padding: 10px 20px;
        }
        </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    f"""
    <div class="navbar">
     </div>
    """,
    unsafe_allow_html=True,
)

open_link_button("Explore More", "https://hrsproject.github.io/home/")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.title("Background Remover")

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
