import os
from pathlib import Path

BASEDIR = Path(os.path.dirname(__file__))


class GRPCConfigs:
    DEBUG = True
    PORT = int(os.environ.get("ENV_GRPC_SERVER_PORT", "50051"))
    WORKERS = int(os.environ.get("ENV_GRPC_SERVER_WORKERS", "30"))
    MAX_MESSAGE_SIZE = 10 * 1000000
    CERTS_PATH = os.environ.get("CERTS", "{}/deployment/certs".format(BASEDIR.parent.parent.parent))
