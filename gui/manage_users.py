import tkinter as tk
from tkinter import messagebox, ttk
import requests

class ManageUsers(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Gestionar Usuarios")
        self.geometry("800x600")
        self.create_widgets()
        self.refresh_users()

    def create_widgets(self):
        self.label = tk.Label(self, text="Gestionar Usuarios", font=("Arial", 18))
        self.label.pack(pady=10)

        self.tree = ttk.Treeview(self, columns=("ID", "Nombre", "DNI", "Semestre", "Correo", "Teléfono"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("DNI", text="DNI")
        self.tree.heading("Semestre", text="Semestre")
        self.tree.heading("Correo", text="Correo")
        self.tree.heading("Teléfono", text="Teléfono")
        self.tree.pack(pady=20, fill=tk.BOTH, expand=True)

        self.refresh_button = tk.Button(self, text="Actualizar", command=self.refresh_users)
        self.refresh_button.pack(side=tk.LEFT, padx=10)

        self.add_button = tk.Button(self, text="Agregar Usuario", command=self.add_user)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.update_button = tk.Button(self, text="Actualizar Usuario", command=self.update_user)
        self.update_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(self, text="Eliminar Usuario", command=self.delete_user)
        self.delete_button.pack(side=tk.LEFT, padx=10)

    def refresh_users(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        response = requests.get("http://localhost:5000/api/usuarios")
        if response.status_code == 200:
            usuarios = response.json()
            for usuario in usuarios:
                self.tree.insert("", tk.END, values=(usuario['id'], usuario['nombre'], usuario['dni'], usuario['semestre'], usuario['correo'], usuario['telefono']))
        else:
            messagebox.showerror("Error", "No se pudo obtener los usuarios")

    def add_user(self):
        AddUserWindow(self)

    def update_user(self):
        selected_item = self.tree.selection()
        if selected_item:
            user_id = self.tree.item(selected_item[0], "values")[0]
            UpdateUserWindow(self, user_id)
        else:
            messagebox.showwarning("Advertencia", "Por favor seleccione un usuario para actualizar")

    def delete_user(self):
        selected_item = self.tree.selection()
        if selected_item:
            user_id = self.tree.item(selected_item[0], "values")[0]
            response = requests.delete(f"http://localhost:5000/api/usuarios/{user_id}")
            if response.status_code == 204:
                messagebox.showinfo("Éxito", "Usuario eliminado exitosamente")
                self.refresh_users()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el usuario")
        else:
            messagebox.showwarning("Advertencia", "Por favor seleccione un usuario para eliminar")

