from wtforms import Form
from flask_wtf import form
from wtforms import StringField,IntegerField, PasswordField, FloatField
from wtforms import EmailField
from wtforms import validators

class UserForm2(Form):
    id=IntegerField("id", [
        validators.number_range(min=1, max=20, message='valor no valido')])
    nombre=StringField("nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=4,max=20,message="Requiere min=4 max=20")
    ])
    apellidos=StringField("apellidos", [
        validators.DataRequired(message="El campo es requerido")
    ])
    email=EmailField("correo", [
        validators.DataRequired(message="El correo es requerido"),
        validators.Email(message="Ingresa correo valido")
    ])
    telefono=StringField("telefono", [
        validators.DataRequired(message="El campo es requerido")
    ])

class MaestroForm(Form):
    matricula = IntegerField("matricula", [
        validators.number_range(min=1, max=99999999, message='valor no valido')
    ])

    nombre = StringField("nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=2, max=50, message="Requiere min=2 max=50")
    ])

    apellidos = StringField("apellidos", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=2, max=50, message="Requiere min=2 max=50")
    ])

    especialidad = StringField("especialidad", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=2, max=50, message="Requiere min=2 max=50")
    ])

    email = EmailField("correo", [
        validators.DataRequired(message="El correo es requerido"),
        validators.Email(message="Ingresa correo valido")
    ])

class CursoForm(Form):
    id = IntegerField("id")
    nombre = StringField("nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=2, max=150, message="Requiere min=2 max=150")
    ])
    descripcion = StringField("descripcion", [
        validators.Optional(),
        validators.length(max=500, message="Máximo 500 caracteres")
    ])
    maestro_id = IntegerField("maestro_id", [
        validators.DataRequired(message="El campo es requerido")
    ])


class InscripcionForm(Form):
    alumno_id = IntegerField("alumno_id", [
        validators.DataRequired(message="El campo es requerido")
    ])
    curso_id = IntegerField("curso_id", [
        validators.DataRequired(message="El campo es requerido")
    ])

