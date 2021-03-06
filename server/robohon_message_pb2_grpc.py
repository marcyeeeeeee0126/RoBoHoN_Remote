# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import robohon_message_pb2 as robohon__message__pb2


class RoBoHoNMessageStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RequestInfo = channel.unary_unary(
        '/robohonmessage.RoBoHoNMessage/RequestInfo',
        request_serializer=robohon__message__pb2.robohon.SerializeToString,
        response_deserializer=robohon__message__pb2.desktop.FromString,
        )


class RoBoHoNMessageServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def RequestInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RoBoHoNMessageServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RequestInfo': grpc.unary_unary_rpc_method_handler(
          servicer.RequestInfo,
          request_deserializer=robohon__message__pb2.robohon.FromString,
          response_serializer=robohon__message__pb2.desktop.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'robohonmessage.RoBoHoNMessage', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
