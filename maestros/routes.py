from flask import render_template, request, redirect, url_for, flash
from . import maestros

import forms
from models import db, Maestros


@maestros.route("/maestros", methods=["GET", "POST"])
def maestros_crud():
    create_form = forms.MaestroForm(request.form)

    if request.method == "POST":
        maes = Maestros(
            matricula=create_form.matricula.data,
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            especialidad=create_form.especialidad.data,
            email=create_form.email.data
        )
        db.session.add(maes)
        db.session.commit()
        return redirect(url_for("maestros.listado_maestros"))

    return render_template("maestros/maestros.html", form=create_form)


@maestros.route("/maestros/listado", methods=["GET"])
def listado_maestros():
    maestros_list = Maestros.query.all()
    return render_template("maestros/listadoMaes.html", maestros=maestros_list)


@maestros.route("/maestros/detalles", methods=["GET"])
def detalles_maestros():
    matricula = request.args.get("matricula", type=int)
    if not matricula:
        return render_template("404.html"), 404

    maes1 = Maestros.query.get(matricula)
    if not maes1:
        return render_template("404.html"), 404

    return render_template(
        "maestros/detallesMaes.html",
        matricula=maes1.matricula,
        nombre=maes1.nombre,
        apellidos=maes1.apellidos,
        especialidad=maes1.especialidad,
        email=maes1.email
    )


@maestros.route("/maestros/modificar", methods=["GET", "POST"])
def modificar_maestros():
    create_form = forms.MaestroForm(request.form)

    if request.method == "GET":
        matricula = request.args.get("matricula", type=int)
        maes1 = Maestros.query.get(matricula) if matricula else None
        if not maes1:
            return render_template("404.html"), 404

        create_form.matricula.data = maes1.matricula
        create_form.nombre.data = (maes1.nombre or "").rstrip()
        create_form.apellidos.data = maes1.apellidos or ""
        create_form.especialidad.data = maes1.especialidad or ""
        create_form.email.data = maes1.email or ""

    if request.method == "POST":
        matricula = create_form.matricula.data
        maes1 = Maestros.query.get(matricula)
        if not maes1:
            return render_template("404.html"), 404

        maes1.nombre = (create_form.nombre.data or "").rstrip()
        maes1.apellidos = create_form.apellidos.data
        maes1.especialidad = create_form.especialidad.data
        maes1.email = create_form.email.data

        db.session.add(maes1)
        db.session.commit()
        return redirect(url_for("maestros.listado_maestros"))

    return render_template("maestros/modificarMaes.html", form=create_form)


@maestros.route("/maestros/eliminar", methods=["GET", "POST"])
def eliminar_maestros():
    create_form = forms.MaestroForm(request.form)

    if request.method == "GET":
        matricula = request.args.get("matricula", type=int)
        maes1 = Maestros.query.get(matricula) if matricula else None
        if not maes1:
            return render_template("404.html"), 404

        create_form.matricula.data = maes1.matricula
        create_form.nombre.data = maes1.nombre
        create_form.apellidos.data = maes1.apellidos
        create_form.especialidad.data = maes1.especialidad
        create_form.email.data = maes1.email

        return render_template("maestros/eliminarMaes.html", form=create_form)

    matricula = create_form.matricula.data
    maes1 = Maestros.query.get(matricula)
    if not maes1:
        return render_template("404.html"), 404

    db.session.delete(maes1)
    db.session.commit()
    return redirect(url_for("maestros.listado_maestros"))