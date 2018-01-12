from flask import request, session
import re
from manage import app


@app.before_request
def process_request1():
    # 1. 获取当前请求url
    current_url = request.path
    # 2. 在配置文件中查看当前请求的URL是否在白名单中
    for url in app.config.get('VALID_URL'):
        if re.match(url, current_url):
            return None
    # 3. 否则的话则进行验证
    permission_dict = session.get("PERMISSION_URL_LIST")

    # 4. 检查用户的请求中是否有需要的session信息，如果没有则redirect到login页面
    