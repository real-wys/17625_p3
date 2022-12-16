import grpc
from service import b_pb2_grpc
import b_pb2
import logging

class RpcClient:
    
    def __init__(self, port):
        print("Client initializing..")
        with grpc.insecure_channel('localhost:'+port) as channel:
            self.stub = b_pb2_grpc.InventoryServiceStub(channel)
        
    def get_book(self, isbn):
        request = b_pb2.GetBookRequest(ISBN=isbn)
        resp = self.stub.GetBook(request)
        return resp