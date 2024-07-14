from flask import request, jsonify
from routes import bp
from models import db, Pedido, DetallePedido
import datetime
from sqlalchemy.exc import IntegrityError

@bp.route('/devoluciones', methods=['POST'])
def add_devolucion():
    data = request.get_json()
    try:
        pedido_id = data['pedido_id']
        detalles = data['detalles']

        pedido = Pedido.query.get_or_404(pedido_id)
        pedido.estado = 'devuelto'
        pedido.detalles += f"\nDevolución: {detalles}"

        for item in data['productos']:
            detalle = DetallePedido.query.filter_by(pedido_id=pedido_id, producto_id=item['producto_id']).first()
            if detalle:
                detalle.cantidad -= item['cantidad']
                if detalle.cantidad <= 0:
                    db.session.delete(detalle)
                else:
                    db.session.add(detalle)

        db.session.commit()
        return jsonify({"message": "Devolución registrada exitosamente"}), 201

    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
