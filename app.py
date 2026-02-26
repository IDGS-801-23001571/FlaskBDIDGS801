from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect

from config import DevelopmentConfig
import forms
from models import db, Alumnos
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route("/")
@app.route("/index")
def index():
    create_form = forms.UserForm2(request.form)
    alumno = Alumnos.query.all()
    return render_template("index.html", form=create_form, alumno=alumno)

@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    create_form = forms.UserForm2(request.form)
    if request.method == "POST":
        alum = Alumnos(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            email=create_form.email.data,
            telefono=create_form.telefono.data
        )
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("Alumnos.html", form=create_form)

@app.route("/detalles", methods=["GET"])
def detalles():
    id = request.args.get("id", type=int)
    if not id:
        return render_template("404.html"), 404

    alum1 = Alumnos.query.get(id)
    if not alum1:
        return render_template("404.html"), 404

    return render_template(
        "detalles.html",
        id=alum1.id,
        nombre=alum1.nombre,
        apellidos=alum1.apellidos,
        email=alum1.email,
        telefono=alum1.telefono
    )

@app.route("/modificar", methods=["GET", "POST"])
def modificar():
    create_form = forms.UserForm2(request.form)

    if request.method == "GET":
        id = request.args.get("id", type=int)
        alum1 = Alumnos.query.get(id) if id else None
        if not alum1:
            return render_template("404.html"), 404

        create_form.id.data = alum1.id
        create_form.nombre.data = (alum1.nombre or "").rstrip()
        create_form.apellidos.data = alum1.apellidos or ""
        create_form.email.data = alum1.email or ""
        create_form.telefono.data = alum1.telefono or ""

    if request.method == "POST":
        id = create_form.id.data
        alum1 = Alumnos.query.get(id)
        if not alum1:
            return render_template("404.html"), 404

        alum1.nombre = (create_form.nombre.data or "").rstrip()
        alum1.apellidos = create_form.apellidos.data
        alum1.email = create_form.email.data
        alum1.telefono = create_form.telefono.data

        db.session.add(alum1)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("modificar.html", form=create_form)

@app.route("/eliminar", methods=["GET", "POST"])
def eliminar():
    create_form = forms.UserForm2(request.form)

    if request.method == "GET":
        id = request.args.get("id", type=int)
        alum1 = Alumnos.query.get(id) if id else None
        if not alum1:
            return render_template("404.html"), 404

        create_form.id.data = alum1.id
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.email.data = alum1.email
        create_form.telefono.data = alum1.telefono
        return render_template("eliminar.html", form=create_form)

    # POST -> borrar
    id = create_form.id.data
    alum1 = Alumnos.query.get(id)
    if not alum1:
        return render_template("404.html"), 404

    db.session.delete(alum1)
    db.session.commit()
    flash("Alumno eliminado correctamente")
    return redirect(url_for("index"))

if __name__ == "__main__":
    csrf.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()