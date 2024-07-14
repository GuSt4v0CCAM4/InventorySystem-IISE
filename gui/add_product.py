import tkinter as tk
from tkinter import messagebox
import requests

class AddProductWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Agregar Producto")
        self.geometry("400x400")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Agregar Nuevo Producto", font=("Arial", 14))
        self.label.pack(pady=10)

        self.fields = ["Código", "Nombre", "Descripción", "Categoría", "Proveedor", "Precio", "Unidad", "Imagen", "Ubicación"]
        self.entries = {}

        for field in self.fields:
            frame = tk.Frame(self)
            frame.pack(pady=5)
            label = tk.Label(frame, text=field)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame)
            entry.pack(side=tk.LEFT)
            self.entries[field] = entry

        self.add_button = tk.Button(self, text="Agregar", command=self.add_product)
        self.add_button.pack(pady=10)

    def add_product(self):
        product_data = {field.lower(): self.entries[field].get() for field in self.fields}
        product_data['precio'] = float(product_data['precio'])

        response = requests.post("http://localhost:5000/api/productos", json=product_data)
        if response.status_code == 201:
            messagebox.showinfo("Éxito", "Producto agregado exitosamente")
            self.master.refresh_products()
            self.destroy()
        else:
            messagebox.showerror("Error", "Error al agregar el producto")

# Código adicional para probar la ventana
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Inventario")
        self.geometry("600x400")

        self.add_product_button = tk.Button(self, text="Agregar Producto", command=self.open_add_product_window)
        self.add_product_button.pack(pady=20)

    def open_add_product_window(self):
        AddProductWindow(self)

    def refresh_products(self):
        # Aquí puedes agregar la lógica para refrescar la lista de productos
        pass

