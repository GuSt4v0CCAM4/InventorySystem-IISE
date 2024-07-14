import tkinter as tk
from tkinter import messagebox
import requests

class AddProductWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add Product")
        self.geometry("400x400")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Add New Product", font=("Arial", 14))
        self.label.pack(pady=10)

        self.fields = ["Codigo", "Nombre", "Descripcion", "Categoria", "Proveedor", "Precio", "Unidad", "Imagen", "Ubicacion"]
        self.entries = {}

        for field in self.fields:
            frame = tk.Frame(self)
            frame.pack(pady=5)
            label = tk.Label(frame, text=field)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame)
            entry.pack(side=tk.LEFT)
            self.entries[field] = entry

        self.add_button = tk.Button(self, text="Add", command=self.add_product)
        self.add_button.pack(pady=10)

    def add_product(self):
        product_data = {field.lower(): self.entries[field].get() for field in self.fields}
        product_data['precio'] = float(product_data['precio'])

        response = requests.post("http://localhost:5000/api/productos", json=product_data)
        if response.status_code == 201:
            messagebox.showinfo("Success", "Product added successfully")
            self.master.refresh_products()
            self.destroy()
        else:
            messagebox.showerror("Error", "Failed to add product")
