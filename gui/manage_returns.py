import tkinter as tk
from tkinter import ttk
import requests
from datetime import datetime
from tkcalendar import DateEntry

class ManageReturns(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Gestionar Devoluciones")
        self.geometry("800x600")
        self.create_widgets()
        self.update_return_table()

    def create_widgets(self):
        tk.Label(self, text="Usuario:").grid(row=0, column=0, sticky=tk.W)
        self.usuario = ttk.Combobox(self)
        self.usuario.grid(row=0, column=1, sticky=tk.W)

        tk.Label(self, text="Producto:").grid(row=1, column=0, sticky=tk.W)
        self.producto = ttk.Combobox(self)
        self.producto.grid(row=1, column=1, sticky=tk.W)

        tk.Label(self, text="Fecha de Devolución:").grid(row=2, column=0, sticky=tk.W)
        self.fecha_devolucion = DateEntry(self, date_pattern='mm/dd/yy')
        self.fecha_devolucion.grid(row=2, column=1, sticky=tk.W)

        tk.Label(self, text="Estado del Producto:").grid(row=3, column=0, sticky=tk.W)
        self.estado_producto = tk.Entry(self)
        self.estado_producto.grid(row=3, column=1, sticky=tk.W)

        tk.Label(self, text="Observaciones:").grid(row=4, column=0, sticky=tk.W)
        self.observaciones = tk.Entry(self)
        self.observaciones.grid(row=4, column=1, sticky=tk.W)

        tk.Button(self, text="Registrar Devolución", command=self.register_return).grid(row=5, column=1, sticky=tk.W)

        self.return_table = ttk.Treeview(self, columns=("ID", "Usuario", "Producto", "Fecha", "Estado", "Observaciones"), show='headings')
        self.return_table.heading("ID", text="ID")
        self.return_table.heading("Usuario", text="Usuario")
        self.return_table.heading("Producto", text="Producto")
        self.return_table.heading("Fecha", text="Fecha")
        self.return_table.heading("Estado", text="Estado")
        self.return_table.heading("Observaciones", text="Observaciones")
        self.return_table.grid(row=6, column=0, columnspan=2, sticky=tk.W+tk.E)

        self.load_comboboxes()

    def load_comboboxes(self):
        try:
            usuarios_response = requests.get("http://localhost:5000/api/usuarios")
            productos_response = requests.get("http://localhost:5000/api/productos")
            if usuarios_response.status_code == 200:
                usuarios = usuarios_response.json()
                self.usuario['values'] = [usuario['nombre'] for usuario in usuarios]
            if productos_response.status_code == 200:
                productos = productos_response.json()
                self.producto['values'] = [producto['nombre'] for producto in productos]
                self.productos_data = productos  # Almacenar datos de productos para referencia
        except Exception as e:
            print("Error al cargar los datos:", str(e))

    def register_return(self):
        try:
            data = {
                'usuario': self.usuario.get(),
                'producto_id': self.productos_data[self.producto.current()]['id'],
                'fecha_devolucion': self.fecha_devolucion.get(),
                'estado_producto': self.estado_producto.get(),
                'observaciones': self.observaciones.get()
            }
            response = requests.post("http://localhost:5000/api/devoluciones", json=data)
            if response.status_code == 201:
                print("Devolución registrada exitosamente.")
                self.update_return_table()
            else:
                print("Error al registrar la devolución:", response.json())
        except Exception as e:
            print("Error al registrar la devolución:", str(e))

    def update_return_table(self):
        for row in self.return_table.get_children():
            self.return_table.delete(row)
        try:
            response = requests.get("http://localhost:5000/api/devoluciones")
            if response.status_code == 200:
                devoluciones = response.json()
                for devolucion in devoluciones:
                    self.return_table.insert('', 'end', values=(devolucion['id'], devolucion['usuario'], devolucion['producto_id'], devolucion['fecha_devolucion'], devolucion['estado_producto'], devolucion['observaciones']))
        except Exception as e:
            print("Error al actualizar la tabla de devoluciones:", str(e))
