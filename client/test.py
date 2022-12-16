import unittest
from unittest import mock
from get_book_titles import get_titles
from inventory_client import RpcClient

class Reply:
    def __init__(self,book):
        self.book = book

class Book:
    def __init__(self, isbn, title):
        self.isbn = isbn
        self.title = title

# mocked return result
resp1 = Reply(Exist=True, book = Book("101", "book1"))
mockReplyNotExistRes = Reply(Book("-1", ""))

class Test_get_book_titles(unittest.TestCase):
    def test_01(self):
        client = RpcClient()
        client.get_book = mock.Mock(return_value = resp1)
        # get book titles based on mock result
        book_title_list = get_titles(client, ["101", "2", "3"])
        self.assertEqual(len(book_title_list), 3)
        self.assertEqual(book_title_list[0], "book1")
        self.assertEqual(book_title_list[1], "N/A")
        self.assertEqual(book_title_list[2], "N/A")


if __name__ == "__main__":
    unittest.main()