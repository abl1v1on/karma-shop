import os
from celery import Celery


"""
Запуск воркеров:
celery -A DjangoCelery worker -l info

Запуск тасков по расписанию:
celery -A DjangoCelery beat -l info
"""


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'KarmaShop.settings')

# Создаем объект celery и даем ему имя 'DjangoCelery' (имя - это название корневой дериктории)
app = Celery('KarmaShop')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое подцепление тасков
app.autodiscover_tasks()


# Рассылка на почту каждые пять минут

# app.conf.beat_schedule = {
#     # Имя таска
#     'send-spam-every-5-minute': {
#         # Путь до нужной таски
#         'task': 'myapp.tasks.send_beat_email',
#         # Переодичность, с которой мы будет отправлять письма
#         'schedule': crontab(minute='*/20')
#     }
# }
