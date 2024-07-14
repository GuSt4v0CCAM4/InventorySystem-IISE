import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests


class InventoryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inventory System")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Inventory Management System", font=("Arial", 18))
        self.label.pack(pady=10)

        self.tree = ttk.Treeview(self, columns=(
        "ID", "Codigo", "Nombre", "Descripcion", "Categoria", "Proveedor", "Precio", "Unidad", "Imagen", "Estado",
        "Ubicacion"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Codigo", text="Codigo")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Descripcion", text="Descripcion")
        self.tree.heading("Categoria", text="Categoria")
        self.tree.heading("Proveedor", text="Proveedor")
        self.tree.heading("Precio", text="Precio")
        self.tree.heading("Unidad", text="Unidad")
        self.tree.heading("Imagen", text="Imagen")
        self.tree.heading("Estado", text="Estado")
        self.tree.heading("Ubicacion", text="Ubicacion")
        self.tree.pack(pady=20, fill=tk.BOTH, expand=True)

        self.refresh_button = tk.Button(self, text="Refresh", command=self.refresh_products)
        self.refresh_button.pack(side=tk.LEFT, padx=10)

        self.add_button = tk.Button(self, text="Add Product", command=self.add_product)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.update_button = tk.Button(self, text="Update Product", command=self.update_product)
        self.update_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(self, text="Delete Product", command=self.delete_product)
        self.delete_button.pack(side=tk.LEFT, padx=10)

    def refresh_products(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        response = requests.get("http://localhost:5000/api/productos")
        if response.status_code == 200:
            products = response.json()
            for product in products:
                self.tree.insert("", tk.END, values=(
                product['id'], product['codigo'], product['nombre'], product['descripcion'], product['categoria'],
                product['proveedor'], product['precio_compra'], product['unidad_medida'], product['imagen'],
                product['estado'], product['ubicacion']))
        else:
            messagebox.showerror("Error", "Failed to fetch products")

    def add_product(self):
        AddProductWindow(self)

    def update_product(self):
        selected_item = self.tree.selection()
        if selected_item:
            product_id = self.tree.item(selected_item[0], "values")[0]
            UpdateProductWindow(self, product_id)
        else:
            messagebox.showwarning("Warning", "Please select a product to update")

    def delete_product(self):
        selected_item = self.tree.selection()
        if selected_item:
            product_id = self.tree.item(selected_item[0], "values")[0]
            response = requests.delete(f"http://localhost:5000/api/productos/{product_id}")
            if response.status_code == 204:
                messagebox.showinfo("Success", "Product deleted successfully")
                self.refresh_products()
            else:
                messagebox.showerror("Error", "Failed to delete product")
        else:
            messagebox.showwarning("Warning", "Please select a product to delete")


class AddProductWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add Product")
        self.geometry("400x400")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Add New Product", font=("Arial", 14))
        self.label.pack(pady=10)

        self.fields = ["Codigo", "Nombre", "Descripcion", "Categoria", "Proveedor", "Precio", "Unidad", "Imagen",
                       "Ubicacion"]
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
            self.destroy()
        else:
            messagebox.showerror("Error", "Failed to add product")


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

        self.fields = ["Codigo", "Nombre", "Descripcion", "Categoria", "Proveedor", "Precio", "Unidad", "Imagen",
                       "Ubicacion"]
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
            self.destroy()
        else:
            messagebox.showerror("Error", "Failed to update product")


if __name__ == "__main__":
    app = InventoryApp()
    app.mainloop()
