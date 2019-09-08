import ibdatastream_pb2_grpc


class Servicer(ibdatastream_pb2_grpc.IBDataStreamServicer):
    def LookUp(self, request, context):
        pass

    def Subscribe(self, request, context):
        pass
