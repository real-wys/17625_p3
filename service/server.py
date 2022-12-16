import asyncio
import logging
import grpc
import b_pb2
import b_pb2_grpc

books = {}

class Issuer(b_pb2_grpc.InventoryServiceServicer) :
    async def CreateBook(self, 
    request:b_pb2.CreateRequest, context:grpc.aio.ServicerContext) -> b_pb2.CreateResponse:
        book = b_pb2.Book(request.ISBN, request.title, request.author,request.genre,request.publishingYear)
        books[request.ISBN] = book
        return b_pb2.CreateResponse(Created=True)
    async def GetBook(self, 
    request:b_pb2.GetBookRequest, context:grpc.aio.ServicerContext) -> b_pb2.GetBookResponse:
        if books.has_key(request.ISBN):
            return b_pb2.GetBookResponse(Exist= True,book=books[request.ISBN])
        return b_pb2.GetBookResponse(Exist=False)

async def serve() -> None:
    server = grpc.aio.server()
    b_pb2_grpc.add_InventoryServiceServicer_to_server(Issuer(), server)
    listen_addr = '[::]:50051'
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()

if __name__ == '__main__':
    b1 = b_pb2.Book(ISBN="010",author="liqi", genre=0, publishingYear=2020, title="b1")
    b2 = b_pb2.Book(ISBN="011",author="liqi", genre=1, publishingYear=2010, title="b2")
    books={b1.ISBN:b1, b2.ISBN:b2}
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())