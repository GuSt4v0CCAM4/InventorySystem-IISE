from flask import request, jsonify
from routes import bp
from models import db, Producto

@bp.route('/productos', methods=['POST'])
def add_producto():
    data = request.get_json()
    nuevo_producto = Producto(
        codigo=data['codigo'],
        nombre=data['nombre'],
        descripcion=data.get('descripcion'),
        categoria=data.get('categoria'),
        proveedor=data.get('proveedor'),
        precio_compra=data.get('precio_compra'),
        unidad_medida=data.get('unidad_medida'),
        imagen=data.get('imagen'),
        estado='disponible',
        ubicacion=data.get('ubicacion')
    )
    db.session.add(nuevo_producto)
    db.session.commit()
    return jsonify(nuevo_producto.id), 201

@bp.route('/productos/<int:id>', methods=['PUT'])
def update_producto(id):
    data = request.get_json()
    producto = Producto.query.get_or_404(id)
    producto.descripcion = data.get('descripcion', producto.descripcion)
    producto.categoria = data.get('categoria', producto.categoria)
    producto.proveedor = data.get('proveedor', producto.proveedor)
    producto.precio_compra = data.get('precio_compra', producto.precio_compra)
    producto.unidad_medida = data.get('unidad_medida', producto.unidad_medida)
    producto.imagen = data.get('imagen', producto.imagen)
    producto.estado = data.get('estado', producto.estado)
    producto.ubicacion = data.get('ubicacion', producto.ubicacion)
    db.session.commit()
    return jsonify({'id': producto.id, 'nombre': producto.nombre, 'descripcion': producto.descripcion})

@bp.route('/productos/<int:id>', methods=['GET'])
def get_producto(id):
    producto = Producto.query.get_or_404(id)
    return jsonify({
        'id': producto.id,
        'codigo': producto.codigo,
        'nombre': producto.nombre,
        'descripcion': producto.descripcion,
        'categoria': producto.categoria,
        'proveedor': producto.proveedor,
        'precio_compra': producto.precio_compra,
        'unidad_medida': producto.unidad_medida,
        'imagen': producto.imagen,
        'estado': producto.estado,
        'ubicacion': producto.ubicacion
    })

@bp.route('/productos', methods=['GET'])
def get_productos():
    productos = Producto.query.all()
    return jsonify([{
        'id': producto.id,
        'codigo': producto.codigo,
        'nombre': producto.nombre,
        'descripcion': producto.descripcion,
        'categoria': producto.categoria,
        'proveedor': producto.proveedor,
        'precio_compra': producto.precio_compra,
        'unidad_medida': producto.unidad_medida,
        'imagen': producto.imagen,
        'estado': producto.estado,
        'ubicacion': producto.ubicacion
    } for producto in productos])
