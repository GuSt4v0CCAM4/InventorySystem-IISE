import tkinter as tk
from tkinter import messagebox, ttk
import requests

class ManageReturns(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Manage Returns")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Manage Returns", font=("Arial", 18))
        self.label.pack(pady=10)

        self.fields = ["Pedido ID", "Detalles", "Productos"]
        self.entries = {}

        for field in self.fields:
            frame = tk.Frame(self)
            frame.pack(pady=5)
            label = tk.Label(frame, text=field)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame)
            entry.pack(side=tk.LEFT)
            self.entries[field] = entry

        self.register_button = tk.Button(self, text="Register Return", command=self.register_return)
        self.register_button.pack(pady=10)

    def register_return(self):
        return_data = {field.lower().replace(' ', '_'): self.entries[field].get() for field in self.fields}
        return_data['productos'] = [{'producto_id': int(p.split(':')[0]), 'cantidad': int(p.split(':')[1])} for p in return_data['productos'].split(',')]
        response = requests.post("http://localhost:5000/api/devoluciones", json=return_data)
        if response.status_code == 201:
            messagebox.showinfo("Success", "Return registered successfully")
            self.destroy()
        else:
            messagebox.showerror("Error", "Failed to register return")
