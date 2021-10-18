import logging


from server import get_db_session
from server.models.user_models import User
from server.rpc.rpc_server.proto_files import rpc_responses_grpc_def_pb2, rpc_responses_grpc_def_pb2_grpc

LOGGER = logging.getLogger("rpc_calls")


class GCPResponseCalls(rpc_responses_grpc_def_pb2_grpc.ResponseCallsServicer):
    """GRPC responses service"""

    def get_users(self, request, context):
        """Get all users"""

        with get_db_session() as session:
            users = session.query(User).all()
            return rpc_responses_grpc_def_pb2.GetUsersResponse(status=200, users=[user.id for user in users])
