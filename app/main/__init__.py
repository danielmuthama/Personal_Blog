from flask import Blueprint, Flask

main = Blueprint('main',__name__)
from . import views, errors
