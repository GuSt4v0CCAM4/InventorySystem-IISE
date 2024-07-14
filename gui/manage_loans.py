import tkinter as tk
from tkinter import messagebox, ttk
import requests

class ManageLoans(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Manage Loans")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Manage Loans", font=("Arial", 18))
        self.label.pack(pady=10)

        self.fields = ["Cliente", "Fecha Pedido", "Detalles", "Productos"]
        self.entries = {}

        for field in self.fields:
            frame = tk.Frame(self)
            frame.pack(pady=5)
            label = tk.Label(frame, text=field)
            label.pack(side=tk.LEFT)
            entry = tk.Entry(frame)
            entry.pack(side=tk.LEFT)
            self.entries[field] = entry

        self.register_button = tk.Button(self, text="Register Loan", command=self.register_loan)
        self.register_button.pack(pady=10)

    def register_loan(self):
        loan_data = {field.lower().replace(' ', '_'): self.entries[field].get() for field in self.fields}
        loan_data['productos'] = [{'producto_id': int(p.split(':')[0]), 'cantidad': int(p.split(':')[1])} for p in loan_data['productos'].split(',')]
        response = requests.post("http://localhost:5000/api/prestamos", json=loan_data)
        if response.status_code == 201:
            messagebox.showinfo("Success", "Loan registered successfully")
            self.destroy()
        else:
            messagebox.showerror("Error", "Failed to register loan")
