from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), unique=True, nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(200), nullable=True)
    categoria = db.Column(db.String(50), nullable=True)
    proveedor = db.Column(db.String(50), nullable=True)
    precio_compra = db.Column(db.Float, nullable=True)
    unidad_medida = db.Column(db.String(20), nullable=True)
    imagen = db.Column(db.String(200), nullable=True)
    estado = db.Column(db.String(20), default='disponible')
    ubicacion = db.Column(db.String(100), nullable=True)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    dni = db.Column(db.String(8), unique=True, nullable=False)
    semestre = db.Column(db.String(10), nullable=True)
    correo = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(15), nullable=True)

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(50), nullable=False)
    fecha_pedido = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    detalles = db.Column(db.String(500), nullable=False)
    estado = db.Column(db.String(20), default='pendiente')
    productos = db.relationship('DetallePedido', backref='pedido', lazy=True)

class DetallePedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    producto = db.relationship('Producto')

class Devolucion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'), nullable=False)
    fecha_devolucion = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    estado_producto = db.Column(db.String(20), nullable=False)
    observaciones = db.Column(db.String(500), nullable=True)
    responsable = db.Column(db.String(50), nullable=False)

class Notificacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    mensaje = db.Column(db.String(500), nullable=False)
    fecha_notificacion = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    estado = db.Column(db.String(20), default='pendiente')
    usuario = db.relationship('Usuario')
