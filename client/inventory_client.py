import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


import grpc
import service.b_pb2 as b__pb2
import service.b_pb2_grpc as b__pb2_grpc


class RpcClient:
    
    def __init__(self, port):
        self.port = port
        self.channel = grpc.insecure_channel(
            '{}:{}'.format("localhost", self.port))
        self.InventoryServiceStub = b__pb2_grpc.InventoryServiceStub(self.channel)
    
    def stub(self):
        return self.InventoryServiceStub
        
    def get_book(self, isbn):
        request = b__pb2.GetBookRequest(ISBN=isbn)
        resp = self.stub.GetBook(request)
        return resp