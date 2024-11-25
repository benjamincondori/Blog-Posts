from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Instancia de la base de datos
db = SQLAlchemy()

def create_app():
    # Crear aplicacion de Flask
    app = Flask(__name__)

    # Configuracion del proyecto
    app.config.from_object('config.Config')

    # Inicializacion de la base de datos
    db.init_app(app)

    # Inicializacion de CKEditor
    from flask_ckeditor import CKEditor
    ckeditor = CKEditor(app)

    # Configuracion de idioma
    import locale
    try:
        locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
    except locale.Error:
        locale.setlocale(locale.LC_ALL, 'C.UTF-8')  # Usa un locale genérico si el específico falla

    # Registrar vistas
    from blog import home
    app.register_blueprint(home.bp)

    from blog import auth
    app.register_blueprint(auth.bp)

    from blog import post
    app.register_blueprint(post.bp)

    # Crear el esquema de tabla en la base de datos
    from blog.models import User, Post

    with app.app_context():
        db.create_all()

    return app

