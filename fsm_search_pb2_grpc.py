# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import fsm_search_pb2 as fsm__search__pb2


class FSMSearchStub(object):
    """The FSMSearch service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddNewFile = channel.unary_unary(
                '/FSMSearch/AddNewFile',
                request_serializer=fsm__search__pb2.AddNewFileRequest.SerializeToString,
                response_deserializer=fsm__search__pb2.AddNewFileResponse.FromString,
                )


class FSMSearchServicer(object):
    """The FSMSearch service definition.
    """

    def AddNewFile(self, request, context):
        """RPC service with request/response information
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FSMSearchServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddNewFile': grpc.unary_unary_rpc_method_handler(
                    servicer.AddNewFile,
                    request_deserializer=fsm__search__pb2.AddNewFileRequest.FromString,
                    response_serializer=fsm__search__pb2.AddNewFileResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FSMSearch', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FSMSearch(object):
    """The FSMSearch service definition.
    """

    @staticmethod
    def AddNewFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FSMSearch/AddNewFile',
            fsm__search__pb2.AddNewFileRequest.SerializeToString,
            fsm__search__pb2.AddNewFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
