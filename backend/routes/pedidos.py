from flask import request, jsonify
from routes import bp
from models import db, Pedido, DetallePedido
import datetime

@bp.route('/pedidos', methods=['POST'])
def add_pedido():
    data = request.get_json()
    nuevo_pedido = Pedido(
        cliente=data['cliente'],
        fecha_pedido=datetime.datetime.strptime(data['fecha_pedido'], '%Y-%m-%d'),
        detalles=data['detalles']
    )
    db.session.add(nuevo_pedido)
    db.session.commit()
    for item in data['productos']:
        detalle = DetallePedido(
            pedido_id=nuevo_pedido.id,
            producto_id=item['producto_id'],
            cantidad=item['cantidad']
        )
        db.session.add(detalle)
    db.session.commit()
    return jsonify(nuevo_pedido.id), 201
