from flask import Flask
from config import Config
from models import db
from routes import bp as api_bp
import threading
from gui.main import InventoryApp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(api_bp, url_prefix='/api')


@app.route('/')
def hello_world():
    return 'Hello, World!'


def run_flask():
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    # Crear la base de datos y las tablas
    with app.app_context():
        db.create_all()

    # Iniciar Flask en un hilo separado
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Iniciar la interfaz gráfica
    inventory_app = InventoryApp()
    inventory_app.mainloop()
