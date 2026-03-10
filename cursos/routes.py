from flask import render_template, request, redirect, url_for, flash
from . import cursos

import forms
from models import db, Curso, Maestros, Alumnos

@cursos.route("/cursos/listado", methods=["GET"])
def listado_cursos():
    cursos_list = Curso.query.all()
    return render_template("cursos/listadoCursos.html", cursos=cursos_list)

@cursos.route("/cursos", methods=["GET", "POST"])
def cursos_crud():
    create_form = forms.CursoForm(request.form)

    if request.method == "POST":
        curso = Curso(
            nombre=create_form.nombre.data,
            descripcion=create_form.descripcion.data,
            maestro_id=create_form.maestro_id.data
        )
        db.session.add(curso)
        db.session.commit()
        return redirect(url_for("cursos.listado_cursos"))

    maestros_list = Maestros.query.all()
    return render_template("cursos/cursos.html", form=create_form, maestros=maestros_list)

@cursos.route("/cursos/detalles", methods=["GET"])
def detalles_curso():
    id = request.args.get("id", type=int)
    curso = Curso.query.get(id) if id else None
    if not curso:
        return render_template("404.html"), 404

    return render_template("cursos/detallesCurso.html", curso=curso)

@cursos.route("/cursos/modificar", methods=["GET", "POST"])
def modificar_curso():
    form = forms.CursoForm(request.form)

    if request.method == "GET":
        id = request.args.get("id", type=int)
        curso = Curso.query.get(id) if id else None
        if not curso:
            return render_template("404.html"), 404

        form.id.data = curso.id
        form.nombre.data = curso.nombre
        form.descripcion.data = curso.descripcion or ""
        form.maestro_id.data = curso.maestro_id

    if request.method == "POST":
        curso = Curso.query.get(form.id.data)
        if not curso:
            return render_template("404.html"), 404

        curso.nombre = form.nombre.data
        curso.descripcion = form.descripcion.data
        curso.maestro_id = form.maestro_id.data

        db.session.add(curso)
        db.session.commit()
        return redirect(url_for("cursos.listado_cursos"))

    maestros_list = Maestros.query.all()
    return render_template("cursos/modificarCurso.html", form=form, maestros=maestros_list)

@cursos.route("/cursos/eliminar", methods=["GET", "POST"])
def eliminar_curso():
    form = forms.CursoForm(request.form)

    if request.method == "GET":
        id = request.args.get("id", type=int)
        curso = Curso.query.get(id) if id else None
        if not curso:
            return render_template("404.html"), 404

        form.id.data = curso.id
        form.nombre.data = curso.nombre
        form.descripcion.data = curso.descripcion or ""
        form.maestro_id.data = curso.maestro_id

        return render_template("cursos/eliminarCurso.html", form=form)

    curso = Curso.query.get(form.id.data)
    if not curso:
        return render_template("404.html"), 404

    db.session.delete(curso)
    db.session.commit()
    return redirect(url_for("cursos.listado_cursos"))

@cursos.route("/inscripciones", methods=["GET", "POST"])
def inscribir():
    form = forms.InscripcionForm(request.form)

    if request.method == "POST":
        curso = Curso.query.get(form.curso_id.data)
        alumno = Alumnos.query.get(form.alumno_id.data)

        if not curso or not alumno:
            return render_template("404.html"), 404

        if alumno in curso.alumnos:
            flash("Ese alumno ya está inscrito en ese curso")
            return redirect(url_for("cursos.inscribir"))

        curso.alumnos.append(alumno)
        db.session.commit()
        return redirect(url_for("cursos.listado_cursos"))

    cursos_list = Curso.query.all()
    alumnos_list = Alumnos.query.all()
    return render_template("cursos/inscribir.html", form=form, cursos=cursos_list, alumnos=alumnos_list)