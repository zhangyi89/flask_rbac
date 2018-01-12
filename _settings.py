import os

DEBUG = False
TESTING = False
VERIFY_EMAIL = True
VERIFY_USER = True

# 配置根目录
ROOT_FOLDER = os.path.dirname(os.path.abspath(__file__))
if os.path.exists('public/static'):
    STATIC_FOLDER = os.path.join(os.getcwd(), 'public', 'static')
else:
    STATIC_FOLDER = os.path.join(ROOT_FOLDER, 'public', 'static')

#: site
SITE_TITLE = 'Flask Project'
SITE_URL = '/'

#: session
# session的相关配置
SESSION_TYPE = 'redis'  # session类型为redis
SESSION_KEY_PREFIX = 'session:'  # 保存到session中的值的前缀
SESSION_PERMANENT = False  # 如果设置为True,则关闭浏览器session就失效
SESSION_USE_SIGNER = False  # 是否对发送到浏览器上session:cookie值进行加密


#: account
# 账户安全的相关配置
SECRET_KEY = 'secret key'
PASSWORD_SECRET = 'password secret'
GRAVATAR_BASE_URL = 'http://www.gravatar.com/avatar'
GRAVATAR_EXTRA = ''

#: sqlalchemy
# orm组件的相关配置
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@127.0.0.1:3306/flaskdb?charset=utf8"
SQLALCHEMY_POOL_SIZE = 2
SQLALCHEMY_POOL_TIMEOUT = 30
SQLALCHEMY_POOL_RECYCLE = -1
# 追踪对象的修改并且发送信号
SQLALCHEMY_TRACK_MODIFICATIONS = False
