import tkinter as tk
from tkinter import messagebox
from flask import Flask
from config import Config
from models import db
from routes import bp as api_bp
import threading

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(api_bp, url_prefix='/api')


@app.route('/')
def hello_world():
    return 'Hello, World!'


def run_flask():
    app.run(host='0.0.0.0')


def on_button_click():
    messagebox.showinfo("Info", "Button clicked!")


def create_gui():
    root = tk.Tk()
    root.title("Inventory System")

    button = tk.Button(root, text="Click Me", command=on_button_click)
    button.pack()

    root.mainloop()


if __name__ == '__main__':
    # Crear la base de datos y las tablas
    with app.app_context():
        db.create_all()

    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    create_gui()
