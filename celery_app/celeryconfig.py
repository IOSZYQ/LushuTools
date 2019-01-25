# import os
# import secretKeys
# from datetime import timedelta
# from celery.schedules import crontab
#
# import djcelery
# djcelery.setup_loader()
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LuShuTools.settings')
#
# # celery  配置
# BROKER_URL = 'redis://{0}:{1}/0'.format(secretKeys.REDIS_HOST, secretKeys.REDIS_PORT)
# CELERY_RESULT_BACKEND = BROKER_URL
# CELERY_TIMEZONE = 'Asia/Shanghai'
# from kombu import Exchange, Queue
#
#
# CELERY_QUEUES = {
#     #定时任务队列
#     'beat_tasks': {
#         'exchange': 'beat_tasks',
#         'exchange_type': 'direct',
#         'binding_key': 'beat_tasks'
#     },
#     #普通任务队列
#     'work_queue': {
#         'exchange': 'work_queue',
#         'exchange_type': 'direct',
#         'binding_key': 'work_queue'
#     }
# }
#
# #默认用普通任务队列
# CELERY_DEFAULT_QUEUE = 'work_queue'
#
# CELERY_IMPORTS = (
#     'apps.Template.tasks',
#     'images.tasks',
# )
#
# # 有些情况可以防止死锁
# CELERYD_FORCE_EXECV = True
#
# # 设置并发的worker数量
# CELERYD_CONCURRENCY = 4
#
# # 允许重试
# CELERY_ACKS_LATE = True
#
# # 每个worker最多执行100个任务被销毁，可以防止内存泄露
# CELERYD_MAX_TASKS_PER_CHILD = 100
#
# # 单个任务的最大运行时间
# CELERYD_TASK_TIME_LIMIT = 12 * 30
#
#
# CELERYBEAT_SCHEDULE = {
#     'send_email': {
#         'task': 'apps.Template.tasks.sendCeleryEmail',
#         'schedule': timedelta(seconds=5),
#         'options': {
#             'queue': 'beat_tasks'
#         }
#     }
# }
