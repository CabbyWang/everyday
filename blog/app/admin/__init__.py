from flask import render_template
from flask import Blueprint

print(2222, __name__)
admin = Blueprint('admin', __name__)

from . import forms, views