from ._base import db

# 导入模式时，可以被使用的字段
__all__ = [
    'Menu', 'Group', 'Permission', 'User', 'Role', 'User2role', 'Role2permission'
]


class Menu(db.Model):
    """菜单组"""
    __tablename__ = 'menu'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(40), unique=True, index=True, nullable=False)

    __table_args__ = {
        'mysql_engine' : 'InnoDB',
        'mysql_charset': 'utf8'
    }

    def __str__(self):
        return self.title


class Group(db.Model):
    """权限组"""
    __tablename__ = 'group'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    caption = db.Column(db.String(40), unique=True, index=True, nullable=False)

    __table_args__ = {
        'mysql_engine' : 'InnoDB',
        'mysql_charset': 'utf8'
    }

    def __str__(self):
        return self.caption


class Permission(db.Model):
    """权限表"""
    __tablename__ = 'permission'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(40))
    url = db.Column(db.String(80), unique=True, index=True)

    menu_gp = db.Column(db.Integer, db.ForeignKey('menu.id'))
    code = db.Column(db.String(40))
    group = db.Column(db.Integer, db.ForeignKey('group.id'))

    __table_args__ = {
        'mysql_engine' : 'InnoDB',
        'mysql_charset': 'utf8'
    }

    def __str__(self):
        return self.title


class User(db.Model):
    """用户表"""
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(40), unique=True, index=True, nullable=False)
    password = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)

    __table_args__ = {
        'mysql_engine' : 'InnoDB',
        'mysql_charset': 'utf8'
    }

    def __str__(self):
        return self.username


class Role(db.Model):
    """角色表"""
    __tablename = 'role'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(40), unique=True, index=True, nullable=False)

    __table_args__ = {
        'mysql_engine' : 'InnoDB',
        'mysql_charset': 'utf8'
    }

    def __str__(self):
        return self.title


class User2role(db.Model):
    """角色和用户关系表"""
    __tablename__ = 'user2role'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    __table_args__ = {
        'mysql_engine' : 'InnoDB',
        'mysql_charset': 'utf8'
    }

    def __str__(self):
        return self.user_id, self.role_id


class Role2permission(db.Model):
    """角色和权限关系表"""
    __tablename__ = 'role2permission'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    permission_id = db.Column(db.Integer, db.ForeignKey('permission.id'))

    __table_args__ = {
        'mysql_engine' : 'InnoDB',
        'mysql_charset': 'utf8'
    }

    def __str__(self):
        return self.role_id, self.permission_id
