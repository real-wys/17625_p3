
from inventory_client import RpcClient

def get_titles(client, ISBNs):
    titles = []
    for isbn in ISBNs:
        b = client.get_book(isbn)
        if b.Exist:
            titles.append(b.book.title)
        else:
            titles.append("N/A")
    return titles

if __name__ == '__main__':
    rpcClient = RpcClient("50051")
    ISBNS = {"011","010","001"}
    res_list = get_titles(rpcClient, ISBNs=ISBNS)