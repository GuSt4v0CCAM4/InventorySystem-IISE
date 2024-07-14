import tkinter as tk
from tkinter import messagebox, ttk
import requests
from gui.add_product import AddProductWindow
from gui.update_product import UpdateProductWindow

class ManageProducts(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gestionar Productos")
        self.geometry("800x600")
        self.create_widgets()
        self.refresh_products()

    def create_widgets(self):
        self.label = tk.Label(self, text="Gestionar Productos", font=("Arial", 18))
        self.label.pack(pady=10)

        self.tree = ttk.Treeview(self, columns=("ID", "Codigo", "Nombre", "Descripcion", "Categoria", "Proveedor", "Precio", "Unidad", "Imagen", "Estado", "Ubicacion"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Codigo", text="Código")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Descripcion", text="Descripción")
        self.tree.heading("Categoria", text="Categoría")
        self.tree.heading("Proveedor", text="Proveedor")
        self.tree.heading("Precio", text="Precio")
        self.tree.heading("Unidad", text="Unidad")
        self.tree.heading("Imagen", text="Imagen")
        self.tree.heading("Estado", text="Estado")
        self.tree.heading("Ubicacion", text="Ubicación")
        self.tree.pack(pady=20, fill=tk.BOTH, expand=True)

        self.refresh_button = tk.Button(self, text="Actualizar", command=self.refresh_products)
        self.refresh_button.pack(side=tk.LEFT, padx=10)

        self.add_button = tk.Button(self, text="Agregar Producto", command=self.add_product)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.update_button = tk.Button(self, text="Actualizar Producto", command=self.update_product)
        self.update_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(self, text="Eliminar Producto", command=self.delete_product)
        self.delete_button.pack(side=tk.LEFT, padx=10)

    def refresh_products(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        response = requests.get("http://localhost:5000/api/productos")
        if response.status_code == 200:
            products = response.json()
            for product in products:
                self.tree.insert("", tk.END, values=(product['id'], product['codigo'], product['nombre'], product['descripcion'], product['categoria'], product['proveedor'], product['precio_compra'], product['unidad_medida'], product['imagen'], product['estado'], product['ubicacion']))
        else:
            messagebox.showerror("Error", "No se pudo obtener los productos")

    def add_product(self):
        AddProductWindow(self)

    def update_product(self):
        selected_item = self.tree.selection()
        if selected_item:
            product_id = self.tree.item(selected_item[0], "values")[0]
            UpdateProductWindow(self, product_id)
        else:
            messagebox.showwarning("Advertencia", "Por favor seleccione un producto para actualizar")

    def delete_product(self):
        selected_item = self.tree.selection()
        if selected_item:
            product_id = self.tree.item(selected_item[0], "values")[0]
            response = requests.delete(f"http://localhost:5000/api/productos/{product_id}")
            if response.status_code == 204:
                messagebox.showinfo("Éxito", "Producto eliminado exitosamente")
                self.refresh_products()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el producto")
        else:
            messagebox.showwarning("Advertencia", "Por favor seleccione un producto para eliminar")

