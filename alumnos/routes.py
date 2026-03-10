from flask import render_template, request, redirect, url_for, flash
from . import alumnos

import forms
from models import db, Alumnos


@alumnos.route("/index", methods=["GET"])
def index():
    create_form = forms.UserForm2(request.form)
    alumno = Alumnos.query.all()
    return render_template("alumnos/index.html", form=create_form, alumno=alumno)


@alumnos.route("/alumnos", methods=["GET", "POST"])
def alumnos_crud():
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
        return redirect(url_for("alumnos.index"))
    return render_template("alumnos/Alumnos.html", form=create_form)


@alumnos.route("/detalles", methods=["GET"])
def detalles():
    id = request.args.get("id", type=int)
    if not id:
        return render_template("404.html"), 404

    alum1 = Alumnos.query.get(id)
    if not alum1:
        return render_template("404.html"), 404

    return render_template(
        "alumnos/detalles.html",
        id=alum1.id,
        nombre=alum1.nombre,
        apellidos=alum1.apellidos,
        email=alum1.email,
        telefono=alum1.telefono,
        cursos=alum1.cursos
    )


@alumnos.route("/modificar", methods=["GET", "POST"])
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
        return redirect(url_for("alumnos.index"))

    return render_template("alumnos/modificar.html", form=create_form)


@alumnos.route("/eliminar", methods=["GET", "POST"])
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
        return render_template("alumnos/eliminar.html", form=create_form)

    id = create_form.id.data
    alum1 = Alumnos.query.get(id)
    if not alum1:
        return render_template("404.html"), 404

    db.session.delete(alum1)
    db.session.commit()
    return redirect(url_for("alumnos.index"))