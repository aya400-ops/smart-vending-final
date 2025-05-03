import streamlit as st

# Product data
products = {
    "1": {"name": "Cheetos", "price": 2, "image": "cheetos.png"},
    "2": {"name": "Pepsi", "price": 3, "image": "pepsi.png"},
    "3": {"name": "Kitkat", "price": 4, "image": "kitkat.png"},
    "4": {"name": "Juice",  "price": 5, "image": "juice.png"},
    "5": {"name": "Water",  "price": 2, "image": "water.png"},
    "6": {"name": "Galaxy", "price": 4, "image": "galaxy.png"},
    "7": {"name": "Mentos", "price": 3, "image": "mentos.png"},
    "8": {"name": "Oreo",   "price": 4, "image": "oreo.png"}
}

st.title("Smart Vending Machine")

cols = st.columns(4)
for i, (pid, pdata) in enumerate(products.items()):
    with cols[i % 4]:
        st.image(pdata["image"], width=100)
        st.write(f"**{pdata['name']}**")
        st.write(f"ID: {pid} | Price: {pdata['price']} SAR")

st.markdown("---")

selected_id = st.text_input("Enter Product ID")
paid = st.number_input("Insert money (SAR)", min_value=0)

if st.button("Buy"):
    if selected_id in products:
        product = products[selected_id]
        if paid >= product["price"]:
            st.success("Thank you for your purchase!")
        else:
            st.error("Declined: Not enough money.")
    else:
        st.error("Declined: Product not found.")
