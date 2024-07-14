from flask import request, jsonify
from routes import bp
from models import db, Pedido, DetallePedido
import datetime
from sqlalchemy.exc import IntegrityError

@bp.route('/pedidos', methods=['POST'])
def add_pedido():
    data = request.get_json()
    try:
        # Iniciar una nueva transacción
        nuevo_pedido = Pedido(
            cliente=data['cliente'],
            fecha_pedido=datetime.datetime.strptime(data['fecha_pedido'], '%Y-%m-%d'),
            detalles=data['detalles']
        )
        db.session.add(nuevo_pedido)
        db.session.commit()  # Obtener el ID del pedido recién creado sin confirmar la transacción

        # Agregar los detalles del pedido
        for item in data['productos']:
            detalle = DetallePedido(
                pedido_id=nuevo_pedido.id,  # Usar el ID del pedido recién creado
                producto_id=item['producto_id'],
                cantidad=item['cantidad']
            )
            db.session.add(detalle)

        db.session.commit()  # Confirmar toda la transacción

        return jsonify(nuevo_pedido.id), 201

    except IntegrityError as e:
        db.session.rollback()  # Revertir la transacción en caso de error
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        db.session.rollback()  # Revertir la transacción en caso de cualquier otro error
        return jsonify({"error": str(e)}), 500
