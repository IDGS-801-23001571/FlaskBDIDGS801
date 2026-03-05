from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect

from config import DevelopmentConfig
import forms
from models import db, Alumnos
from flask_migrate import Migrate
from maestros.routes import maestros
from alumnos.routes import alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(maestros)
app.register_blueprint(alumnos)
db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    csrf.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()