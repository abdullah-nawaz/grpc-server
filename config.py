import os


class EncryptionConfig:
    SALT_LENGTH = 32
    DERIVATION_ROUNDS = 100000
    BLOCK_SIZE = 16
    KEY_SIZE = 32
    SECRET = "nw2FrNshF"


class MYSQLConfig:
    MYSQLDB_PARAMS = {
        "MYSQLDB_USER": os.environ.get("ENV_MYSQL_USER", "root"),
        "MYSQLDB_PASSWORD": os.environ.get("ENV_MYSQL_PASSWORD", "admin123"),
        "MYSQLDB_HOST": os.environ.get("ENV_MYSQLDB_HOST", "grpc_server-mysqldb"),
        "MYSQLDB_PORT": os.environ.get("ENV_MYSQLDB_PORT", "3306"),
        "MYSQLDB_NAME": os.environ.get("MYSQL_DATABASE", "grpcserverdb")
    }

    MYSQLDB_URL = \
        "mysql+mysqldb://{MYSQLDB_USER}:{MYSQLDB_PASSWORD}@{MYSQLDB_HOST}:{MYSQLDB_PORT}/{MYSQLDB_NAME}".format(
            **MYSQLDB_PARAMS
        )


class SQLAlchemyConfig:
    # This is good, dont need to change it for prod
    SQLALCHEMY_POOL_RECYCLE = int(os.environ.get("ENV_SQLALCHEMY_POOL_RECYCLE", "400"))
    SQLALCHEMY_POOL_TIMEOUT = int(os.environ.get("ENV_SQLALCHEMY_POOL_TIMEOUT", "450"))
    SQLALCHEMY_POOL_SIZE = int(os.environ.get("ENV_SQLALCHEMY_POOL_SIZE", "20"))
    SQLALCHEMY_MAX_OVERFLOW = int(os.environ.get("ENV_SQLALCHEMY_MAX_OVERFLOW", "0"))


class RabbitMQConfig:
    RABBITMQ_PARAMS = {
        "RABBITMQ_HOST": os.environ.get("ENV_RABBITMQ_HOST", "grpc_server-rabbitmq"),
        "RABBITMQ_USER": os.environ.get("ENV_RABBITMQ_USER", "guest"),
        "RABBITMQ_PASSWORD": os.environ.get("ENV_RABBITMQ_PASSWORD", "guest"),
    }

    RABBITMQ_URL = "amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:5672//".format(
        **RABBITMQ_PARAMS
    )
