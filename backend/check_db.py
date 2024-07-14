from app import app
from models import db, Producto
from sqlalchemy.sql import text

with app.app_context():
    # Verificar conexión
    with db.engine.connect() as connection:
        result = connection.execute(text('SELECT 1')).scalar()
        print(f"Connection test result: {result}")

    # Verificar contenido de la tabla
    productos = Producto.query.all()
    print(f"Productos: {productos}")
