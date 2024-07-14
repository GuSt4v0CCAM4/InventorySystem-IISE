from flask import request, jsonify
from routes import bp
from models import db, Pedido, DetallePedido, Usuario, Producto
import datetime
from sqlalchemy.exc import IntegrityError

@bp.route('/prestamos', methods=['POST'])
def add_prestamo():
    data = request.get_json()
    try:
        nuevo_prestamo = Pedido(
            cliente=data['cliente'],
            fecha_pedido=datetime.datetime.strptime(data['fecha_pedido'], '%Y-%m-%d'),
            detalles=data['detalles']
        )
        db.session.add(nuevo_prestamo)
        db.session.commit()

        for item in data['productos']:
            detalle = DetallePedido(
                pedido_id=nuevo_prestamo.id,
                producto_id=item['producto_id'],
                cantidad=item['cantidad']
            )
            db.session.add(detalle)

        db.session.commit()
        return jsonify(nuevo_prestamo.id), 201

    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
