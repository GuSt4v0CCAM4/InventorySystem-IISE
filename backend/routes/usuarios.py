from flask import request, jsonify
from routes import bp
from models import db, Usuario

@bp.route('/usuarios', methods=['POST'])
def add_usuario():
    data = request.get_json()
    nuevo_usuario = Usuario(
        nombre=data['nombre'],
        dni=data['dni'],
        semestre=data.get('semestre'),
        correo=data['correo'],
        telefono=data.get('telefono')
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify(nuevo_usuario.id), 201

@bp.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    data = request.get_json()
    usuario = Usuario.query.get_or_404(id)
    usuario.nombre = data.get('nombre', usuario.nombre)
    usuario.dni = data.get('dni', usuario.dni)
    usuario.semestre = data.get('semestre', usuario.semestre)
    usuario.correo = data.get('correo', usuario.correo)
    usuario.telefono = data.get('telefono', usuario.telefono)
    db.session.commit()
    return jsonify({'id': usuario.id, 'nombre': usuario.nombre, 'correo': usuario.correo})

@bp.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    return jsonify({
        'id': usuario.id,
        'nombre': usuario.nombre,
        'dni': usuario.dni,
        'semestre': usuario.semestre,
        'correo': usuario.correo,
        'telefono': usuario.telefono
    })

@bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{
        'id': usuario.id,
        'nombre': usuario.nombre,
        'dni': usuario.dni,
        'semestre': usuario.semestre,
        'correo': usuario.correo,
        'telefono': usuario.telefono
    } for usuario in usuarios])
