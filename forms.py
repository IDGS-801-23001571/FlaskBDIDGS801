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

