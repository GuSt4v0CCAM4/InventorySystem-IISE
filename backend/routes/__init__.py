from flask import Blueprint

bp = Blueprint('api', __name__)

# Importa las rutas
import routes.productos
import routes.usuarios
import routes.pedidos
import routes.reportes
import routes.prestamos
import routes.devoluciones
