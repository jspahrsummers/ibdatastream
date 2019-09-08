from . import ibdatastream_pb2, ibdatastream_pb2_grpc


class Servicer(ibdatastream_pb2_grpc.IBDataStreamServicer):
    def LookUp(self, request, context):
        return ibdatastream_pb2.Contract(contractID=0)

    def Subscribe(self, request, context):
        pass
