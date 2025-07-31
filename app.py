import streamlit as st
from PIL import Image
from ocr_utils import extract_text_from_image
from api_utils import fetch_product_details
import pytesseract

# Add this line before using pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


st.set_page_config(page_title="OCR Product Info Scanner", layout="centered")
st.title(" OCR-based Product Information Scanner")

uploaded_file = st.file_uploader("Upload an image (e.g. product label)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)


    with st.spinner(" Extracting text using OCR..."):
        extracted_text = extract_text_from_image(image)
        st.markdown("####  Extracted Text:")
        st.code(extracted_text)

        if extracted_text.strip():
            with st.spinner(" Searching Open Food Facts..."):
                product_data = fetch_product_details(extracted_text)
                if product_data:
                    st.success(" Product Found!")
                    st.markdown(f"**Product Name:** {product_data.get('product_name', 'N/A')}")
                    st.markdown(f"**Brands:** {product_data.get('brands', 'N/A')}")
                    st.markdown(f"**Categories:** {product_data.get('categories', 'N/A')}")
                    st.markdown(f"**Nutri-Score:** {product_data.get('nutriscore_grade', 'N/A')}")
                    if product_data.get("image_url"):
                        st.image(product_data["image_url"], caption="Product Image")
                else:
                    st.error("No matching product found.")
        else:
            st.warning("No readable text found. Please try another image.")