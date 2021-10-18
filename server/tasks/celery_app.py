from celery import Celery

from config import RabbitMQConfig

celery_app = Celery(
    "grpc_server_celery",
    broker=RabbitMQConfig.RABBITMQ_URL,
    include=[]
)


# celery_app.conf.beat_schedule = {
#     'run_workflow_manager': {
#         'task': 'workflow_manager',
#         'schedule': 3.0,
#         'options': {'queue': 'workflow_queue'}
#     }
# }
