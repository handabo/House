import pymysql
import celery
import os

from fang import settings

pymysql.install_as_MySQLdb()

# 注册环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fang.settings')

app = celery.Celery('fang',
                    backend='amqp://hanbo:123456@120.77.222.217:5672/vhost1'
)

# 从默认的配置文件读取配置信息
app.config_from_object('django.conf:settings')

# Celery加载所有注册的应用
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)