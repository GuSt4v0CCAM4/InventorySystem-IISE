import tkinter as tk
from tkinter import messagebox
import requests

class UpdateProductWindow(tk.Toplevel):
    def __init__(self, parent, product_id):
        super().__init__(parent)
        self.product_id = product_id
        self.title("Update Product")
        self.geometry("400x400")
        self.create_widgets()
        self.load_product_data()

    def create_widgets(self):
        self.label = tk.Label(self, text="Update Product", font=("Arial", 14))
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

        self.update_button = tk.Button(self, text="Update", command=self.update_product)
        self.update_button.pack(pady=10)

    def load_product_data(self):
        response = requests.get(f"http://localhost:5000/api/productos/{self.product_id}")
        if response.status_code == 200:
            product = response.json()
            for field in self.fields:
                self.entries[field].insert(0, product[field.lower()])

    def update_product(self):
        product_data = {field.lower(): self.entries[field].get() for field in self.fields}
        product_data['precio'] = float(product_data['precio'])

        response = requests.put(f"http://localhost:5000/api/productos/{self.product_id}", json=product_data)
        if response.status_code == 200:
            messagebox.showinfo("Success", "Product updated successfully")
            self.master.refresh_products()
            self.destroy()
        else:
            messagebox.showerror("Error", "Failed to update product")
