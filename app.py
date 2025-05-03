import streamlit as st
from PIL import Image

st.set_page_config(page_title="Smart Vending Machine", layout="centered")

st.title("Smart Vending Machine")

# Status message
status = st.empty()

# Product list
products = {
    "1": {"name": "Cheetos", "price": 2, "image": "images/cheetos.png"},
    "2": {"name": "Pepsi", "price": 3, "image": "images/pepsi.png"},
    "3": {"name": "Kitkat", "price": 4, "image": "images/kitkat.png"},
    "4": {"name": "Juice",  "price": 5, "image": "images/juice.png"},
    "5": {"name": "Water",  "price": 2, "image": "images/water.png"},
    "6": {"name": "Galaxy", "price": 4, "image": "images/galaxy.png"},
    "7": {"name": "Mentos", "price": 3, "image": "images/mentos.png"},
    "8": {"name": "Oreo",   "price": 4, "image": "images/oreo.png"}
}

st.markdown("### Products Inside the Machine:")

# Show vending machine graphic
st.image("images/vending_machine.png", use_column_width=True)

# Show products in 2 rows (4 each)
cols = st.columns(4)
for i, (pid, data) in enumerate(products.items()):
    with cols[i % 4]:
        st.image(data["image"], width=100)
        st.markdown(f"**{data['name']}**")
        st.markdown(f"ID: {pid} | {data['price']} SAR")

st.markdown("---")
st.markdown("### Select a Product Number:")

col_buttons = st.columns(8)
for i in range(1, 9):
    with col_buttons[i-1]:
        if st.button(str(i)):
            product = products.get(str(i))
            if product:
                status.success(f"Purchase Approved: {product['name']}")
            else:
                status.error("Declined: Product not found.")
