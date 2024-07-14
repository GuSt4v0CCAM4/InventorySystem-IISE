import tkinter as tk
from tkinter import ttk
import requests
from datetime import datetime
from tkcalendar import DateEntry

class ManageLoans(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Gestionar Préstamos")
        self.geometry("800x600")
        self.create_widgets()
        self.update_loan_table()

    def create_widgets(self):
        tk.Label(self, text="Cliente:").grid(row=0, column=0, sticky=tk.W)
        self.cliente = ttk.Combobox(self)
        self.cliente.grid(row=0, column=1, sticky=tk.W)

        tk.Label(self, text="Fecha del Pedido:").grid(row=1, column=0, sticky=tk.W)
        self.fecha_pedido = DateEntry(self, date_pattern='dd/mm/yy')
        self.fecha_pedido.grid(row=1, column=1, sticky=tk.W)

        tk.Label(self, text="Detalles:").grid(row=2, column=0, sticky=tk.W)
        self.detalles = tk.Entry(self)
        self.detalles.grid(row=2, column=1, sticky=tk.W)

        tk.Label(self, text="Productos:").grid(row=3, column=0, sticky=tk.W)
        self.productos = tk.Listbox(self, selectmode=tk.MULTIPLE)
        self.productos.grid(row=3, column=1, sticky=tk.W)

        tk.Button(self, text="Registrar Préstamo", command=self.register_loan).grid(row=4, column=1, sticky=tk.W)

        self.loan_table = ttk.Treeview(self, columns=("ID", "Cliente", "Fecha", "Detalles", "Productos"), show='headings')
        self.loan_table.heading("ID", text="ID")
        self.loan_table.heading("Cliente", text="Cliente")
        self.loan_table.heading("Fecha", text="Fecha")
        self.loan_table.heading("Detalles", text="Detalles")
        self.loan_table.heading("Productos", text="Productos")
        self.loan_table.grid(row=5, column=0, columnspan=2, sticky=tk.W+tk.E)

        self.load_comboboxes()

    def load_comboboxes(self):
        try:
            usuarios_response = requests.get("http://localhost:5000/api/usuarios")
            productos_response = requests.get("http://localhost:5000/api/productos")
            if usuarios_response.status_code == 200:
                usuarios = usuarios_response.json()
                self.cliente['values'] = [usuario['nombre'] for usuario in usuarios]
            if productos_response.status_code == 200:
                productos = productos_response.json()
                for producto in productos:
                    self.productos.insert(tk.END, producto['nombre'])
                self.productos_data = productos  # Almacenar datos de productos para referencia
        except Exception as e:
            print("Error al cargar los datos:", str(e))

    def register_loan(self):
        try:
            selected_indices = self.productos.curselection()
            selected_productos = [{'producto_id': self.productos_data[i]['id'], 'cantidad': 1} for i in selected_indices]
            data = {
                'cliente': self.cliente.get(),
                'fecha_pedido': self.fecha_pedido.get(),
                'detalles': self.detalles.get(),
                'productos': selected_productos
            }
            response = requests.post("http://localhost:5000/api/prestamos", json=data)
            if response.status_code == 201:
                print("Préstamo registrado exitosamente.")
                self.update_loan_table()
            else:
                print("Error al registrar el préstamo:", response.json())
        except Exception as e:
            print("Error al registrar el préstamo:", str(e))

    def update_loan_table(self):
        for row in self.loan_table.get_children():
            self.loan_table.delete(row)
        try:
            response = requests.get("http://localhost:5000/api/prestamos")
            if response.status_code == 200:
                prestamos = response.json()
                for prestamo in prestamos:
                    productos_str = ', '.join([str(p['producto_id']) + ': ' + str(p['cantidad']) for p in prestamo['productos']])
                    self.loan_table.insert('', 'end', values=(prestamo['id'], prestamo['cliente'], prestamo['fecha_pedido'], prestamo['detalles'], productos_str))
        except Exception as e:
            print("Error al actualizar la tabla de préstamos:", str(e))

