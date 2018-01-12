from flask import request, Blueprint
from flask import render_template

from ..service.init_permission import init_permission

__all__ = ['bp']

bp = Blueprint('/login', __name__)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        # 验证用户名和密码
        user = request.form.get('username')
        # 如果验证成功则写入权限
        init_permission(user)
