import os
import pathlib

base_dir = os.path.abspath(os.path.dirname(__file__))
a = pathlib.Path(base_dir, 'data.sql')

class Config:
    SECRET_KEY = 'a string'
    # sql config
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(str(a))
    SQLALCHEMY_COMMIT_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass
