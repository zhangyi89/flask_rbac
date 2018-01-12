
from flask import Flask

from .models._base import db


def create_app(config=None):
    app = Flask(__name__, template_folder='templates', )

    app.debug = True
    app.secret_key = 'session'
    # 设置配置文件
    app.config.from_pyfile('_settings.py')

    # 注册蓝图
    register_routes(app)
    # 注册组件

    # 注册数据库
    register_database(app)

    return app

def register_database(app):
    """Database related configuration"""
    db.init_app(app)


def register_routes(app):
    pass

