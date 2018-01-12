from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from rbac.app import create_app
from rbac.models._base import db

app = create_app()

# 创建migrate示例
migrate = Migrate(app, db)


# 创建命令管理器
manager = Manager(app)

# 创建db命令
manager.add_command('db', MigrateCommand)
"""
数据库迁移命令
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade
"""

# 创建启动命令
manager.add_command('runserver', Server())
"""
自定义命令
    python manage.py runserver 
"""


if __name__ == '__main__':
    manager.run()
