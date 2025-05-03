
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# المنتجات (الكمية يمكن تعديلها)
products = {
    1: {"name": "Juice", "price": "5 SAR", "stock": 2, "image": "juice.png"},
    2: {"name": "Water", "price": "2 SAR", "stock": 3, "image": "water.png"},
    3: {"name": "Galaxy", "price": "6 SAR", "stock": 1, "image": "galaxy.png"},
    4: {"name": "Mentos", "price": "3 SAR", "stock": 0, "image": "mentos.png"},
    5: {"name": "Cheetos", "price": "4 SAR", "stock": 2, "image": "cheetos.png"},
    6: {"name": "Oreo", "price": "5 SAR", "stock": 1, "image": "oreo.png"},
    7: {"name": "KitKat", "price": "5 SAR", "stock": 0, "image": "kitkat.png"},
    8: {"name": "Pepsi", "price": "4 SAR", "stock": 5, "image": "pepsi.png"},
}

def pay():
    try:
        product_id = int(entry.get())
        if product_id not in products:
            screen_var.set("Declined: Product Not Found")
        elif products[product_id]["stock"] <= 0:
            screen_var.set("Declined: Out of Stock")
        else:
            products[product_id]["stock"] -= 1
            screen_var.set(f"Accepted: Enjoy {products[product_id]['name']}")
    except:
        screen_var.set("Please enter a number")

root = tk.Tk()
root.title("Smart Vending Machine")
root.geometry("950x700")
root.configure(bg="gray")

# شاشة الآلة
screen_var = tk.StringVar()
screen_var.set("Welcome!")
screen = tk.Label(root, textvariable=screen_var, bg="black", fg="white", font=("Arial", 18), width=30, height=2)
screen.pack(pady=10)

# المنتجات
frame = tk.Frame(root, bg="gray")
frame.pack()

row = 0
col = 0
for pid in sorted(products):
    data = products[pid]
    try:
        img = Image.open(data["image"]).resize((140, 140))
        photo = ImageTk.PhotoImage(img)
        panel = tk.Label(frame, image=photo)
        panel.image = photo
        panel.grid(row=row, column=col, padx=15, pady=10)

        info = tk.Label(frame, text=f"{pid}. {data['name']}\n{data['price']}", font=("Arial", 10), bg="white", width=20)
        info.grid(row=row+1, column=col)
        col += 1
        if col == 4:
            col = 0
            row += 2
    except:
        continue

# مدخل رقم المنتج
entry_label = tk.Label(root, text="Enter product number:", bg="gray", font=("Arial", 12))
entry_label.pack(pady=(20, 5))
entry = tk.Entry(root, font=("Arial", 14), width=10)
entry.pack()

# زر الدفع
pay_btn = tk.Button(root, text="Insert Card / Pay", font=("Arial", 14), command=pay, bg="green", fg="white")
pay_btn.pack(pady=20)

root.mainloop()
