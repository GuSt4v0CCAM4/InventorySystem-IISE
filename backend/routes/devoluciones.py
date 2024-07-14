from flask import request, jsonify
from routes import bp
import datetime
import traceback

devoluciones_temporales = []

@bp.route('/devoluciones', methods=['POST'])
def add_devolucion():
    data = request.get_json()
    try:
        print("Datos recibidos para la devolución:", data)
        fecha_devolucion = datetime.datetime.strptime(data['fecha_devolucion'], '%m/%d/%y').strftime('%Y-%m-%d')
        nueva_devolucion = {
            'id': len(devoluciones_temporales) + 1,
            'usuario': data['usuario'],
            'producto_id': data['producto_id'],
            'fecha_devolucion': fecha_devolucion,
            'estado_producto': data['estado_producto'],
            'observaciones': data['observaciones']
        }
        devoluciones_temporales.append(nueva_devolucion)

        print("Devolución añadida con ID:", nueva_devolucion['id'])
        return jsonify(nueva_devolucion['id']), 201

    except Exception as e:
        print("Error general:", str(e))
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@bp.route('/devoluciones', methods=['GET'])
def get_devoluciones():
    return jsonify(devoluciones_temporales)
