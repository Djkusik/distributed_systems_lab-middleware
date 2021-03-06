# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import match_pb2 as match__pb2


class ScoreNotificationsStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubscribeToTournament = channel.unary_stream(
                '/ScoreNotifications/SubscribeToTournament',
                request_serializer=match__pb2.SubscribeRequest.SerializeToString,
                response_deserializer=match__pb2.ScoreReply.FromString,
                )


class ScoreNotificationsServicer(object):
    """Missing associated documentation comment in .proto file"""

    def SubscribeToTournament(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ScoreNotificationsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SubscribeToTournament': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeToTournament,
                    request_deserializer=match__pb2.SubscribeRequest.FromString,
                    response_serializer=match__pb2.ScoreReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ScoreNotifications', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ScoreNotifications(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def SubscribeToTournament(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/ScoreNotifications/SubscribeToTournament',
            match__pb2.SubscribeRequest.SerializeToString,
            match__pb2.ScoreReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
