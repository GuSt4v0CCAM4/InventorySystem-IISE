import tkinter as tk
from gui.manage_products import ManageProducts
from gui.manage_users import ManageUsers
from gui.manage_loans import ManageLoans
from gui.manage_returns import ManageReturns

class InventoryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Inventario")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Sistema de Gestión de Inventario", font=("Arial", 18))
        self.label.pack(pady=10)

        self.manage_products_button = tk.Button(self, text="Gestionar Productos", command=self.open_manage_products)
        self.manage_products_button.pack(pady=10)

        self.manage_users_button = tk.Button(self, text="Gestionar Usuarios", command=self.open_manage_users)
        self.manage_users_button.pack(pady=10)

        self.manage_loans_button = tk.Button(self, text="Gestionar Préstamos", command=self.open_manage_loans)
        self.manage_loans_button.pack(pady=10)

        self.manage_returns_button = tk.Button(self, text="Gestionar Devoluciones", command=self.open_manage_returns)
        self.manage_returns_button.pack(pady=10)

    def open_manage_products(self):
        ManageProducts(self)

    def open_manage_users(self):
        ManageUsers(self)

    def open_manage_loans(self):
        ManageLoans(self)

    def open_manage_returns(self):
        ManageReturns(self)
