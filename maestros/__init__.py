from flask import Blueprint
from models import Maestros

maestros=Blueprint(
    'maestros',
    __name__,
    template_folder='templates',
    static_folder='static')
from . import routes