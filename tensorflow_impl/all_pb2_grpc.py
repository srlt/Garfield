# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import all_pb2 as all__pb2


class TrainMessageExchangeStub(object):
  """This service is a general one. It includes all information that is required to be transferred between the PS and workers

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetPublicKey = channel.unary_unary(
        '/TrainMessageExchange/GetPublicKey',
        request_serializer=all__pb2.Empty.SerializeToString,
        response_deserializer=all__pb2.PublicKey.FromString,
        )
    self.GetUnifiedModel = channel.unary_unary(
        '/TrainMessageExchange/GetUnifiedModel',
        request_serializer=all__pb2.Empty.SerializeToString,
        response_deserializer=all__pb2.Model.FromString,
        )
    self.GetCompleteModel = channel.unary_unary(
        '/TrainMessageExchange/GetCompleteModel',
        request_serializer=all__pb2.Request.SerializeToString,
        response_deserializer=all__pb2.CompleteModel.FromString,
        )
    self.GetOnlyHash = channel.unary_unary(
        '/TrainMessageExchange/GetOnlyHash',
        request_serializer=all__pb2.Request.SerializeToString,
        response_deserializer=all__pb2.CompleteModel.FromString,
        )
    self.GetGradHashes = channel.unary_unary(
        '/TrainMessageExchange/GetGradHashes',
        request_serializer=all__pb2.Request.SerializeToString,
        response_deserializer=all__pb2.GradHashes.FromString,
        )
    self.GetGradHash = channel.unary_unary(
        '/TrainMessageExchange/GetGradHash',
        request_serializer=all__pb2.Request.SerializeToString,
        response_deserializer=all__pb2.GradHash.FromString,
        )
    self.GetGradients = channel.unary_unary(
        '/TrainMessageExchange/GetGradients',
        request_serializer=all__pb2.Request.SerializeToString,
        response_deserializer=all__pb2.Gradients.FromString,
        )
    self.GetModel = channel.unary_unary(
        '/TrainMessageExchange/GetModel',
        request_serializer=all__pb2.Request.SerializeToString,
        response_deserializer=all__pb2.Model.FromString,
        )


class TrainMessageExchangeServicer(object):
  """This service is a general one. It includes all information that is required to be transferred between the PS and workers

  """

  def GetPublicKey(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUnifiedModel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCompleteModel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetOnlyHash(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetGradHashes(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetGradHash(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetGradients(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetModel(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TrainMessageExchangeServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetPublicKey': grpc.unary_unary_rpc_method_handler(
          servicer.GetPublicKey,
          request_deserializer=all__pb2.Empty.FromString,
          response_serializer=all__pb2.PublicKey.SerializeToString,
      ),
      'GetUnifiedModel': grpc.unary_unary_rpc_method_handler(
          servicer.GetUnifiedModel,
          request_deserializer=all__pb2.Empty.FromString,
          response_serializer=all__pb2.Model.SerializeToString,
      ),
      'GetCompleteModel': grpc.unary_unary_rpc_method_handler(
          servicer.GetCompleteModel,
          request_deserializer=all__pb2.Request.FromString,
          response_serializer=all__pb2.CompleteModel.SerializeToString,
      ),
      'GetOnlyHash': grpc.unary_unary_rpc_method_handler(
          servicer.GetOnlyHash,
          request_deserializer=all__pb2.Request.FromString,
          response_serializer=all__pb2.CompleteModel.SerializeToString,
      ),
      'GetGradHashes': grpc.unary_unary_rpc_method_handler(
          servicer.GetGradHashes,
          request_deserializer=all__pb2.Request.FromString,
          response_serializer=all__pb2.GradHashes.SerializeToString,
      ),
      'GetGradHash': grpc.unary_unary_rpc_method_handler(
          servicer.GetGradHash,
          request_deserializer=all__pb2.Request.FromString,
          response_serializer=all__pb2.GradHash.SerializeToString,
      ),
      'GetGradients': grpc.unary_unary_rpc_method_handler(
          servicer.GetGradients,
          request_deserializer=all__pb2.Request.FromString,
          response_serializer=all__pb2.Gradients.SerializeToString,
      ),
      'GetModel': grpc.unary_unary_rpc_method_handler(
          servicer.GetModel,
          request_deserializer=all__pb2.Request.FromString,
          response_serializer=all__pb2.Model.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'TrainMessageExchange', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
