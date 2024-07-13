from flask import jsonify
from routes import bp
from models import db, DetallePedido, Producto

@bp.route('/reportes/stock', methods=['GET'])
def generar_reporte_stock():
    movimientos = DetallePedido.query.all()
    reporte = []
    for movimiento in movimientos:
        producto = Producto.query.get(movimiento.producto_id)
        reporte.append({
            'producto': producto.nombre,
            'cantidad': movimiento.cantidad,
            'fecha': movimiento.pedido.fecha_pedido,
            'cliente': movimiento.pedido.cliente,
            'estado': movimiento.pedido.estado
        })
    return jsonify(reporte)
