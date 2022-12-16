
from inventory_client import RpcClient

class GetBook:
    def get_titles(rpcClient, ISBNs):
        stub = rpcClient.stub()
        titles = []
        for isbn in ISBNs:
            b = stub.GetBook(isbn)
            if b.Exist:
                titles.append(b.book.title)
            else:
                titles.append("N/A")
        return titles

if __name__ == '__main__':
    rpcClient = RpcClient(50051)
    ISBNS = {"011","010","001"}
    res_list = get_titles(rpcClient, ISBNs=ISBNS)