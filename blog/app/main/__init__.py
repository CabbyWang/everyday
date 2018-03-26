from flask import Blueprint

print(1111, __name__)
main = Blueprint('main', __name__)

from . import views, errors