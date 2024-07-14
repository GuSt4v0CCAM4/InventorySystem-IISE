from flask import request, jsonify
from routes import bp
from models import Pedido, DetallePedido
import datetime
import traceback

prestamos_temporales = []

@bp.route('/prestamos', methods=['POST'])
def add_prestamo():
    data = request.get_json()
    try:
        print("Datos recibidos para el préstamo:", data)
        fecha_pedido = datetime.datetime.strptime(data['fecha_pedido'], '%m/%d/%y').strftime('%Y-%m-%d')
        nuevo_prestamo = {
            'id': len(prestamos_temporales) + 1,
            'cliente': data['cliente'],
            'fecha_pedido': fecha_pedido,
            'detalles': data['detalles'],
            'productos': data['productos']
        }
        prestamos_temporales.append(nuevo_prestamo)

        print("Préstamo añadido con ID:", nuevo_prestamo['id'])
        return jsonify(nuevo_prestamo['id']), 201

    except Exception as e:
        print("Error general:", str(e))
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@bp.route('/prestamos', methods=['GET'])
def get_prestamos():
    return jsonify(prestamos_temporales)
