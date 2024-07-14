import tkinter as tk
from gui.manage_products import ManageProducts

class InventoryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inventory System")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Inventory Management System", font=("Arial", 18))
        self.label.pack(pady=10)

        self.manage_products_button = tk.Button(self, text="Manage Products", command=self.open_manage_products)
        self.manage_products_button.pack(pady=10)

    def open_manage_products(self):
        ManageProducts(self)

if __name__ == "__main__":
    app = InventoryApp()
    app.mainloop()
