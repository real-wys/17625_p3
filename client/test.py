import unittest
from unittest.mock import MagicMock
from unittest import TestCase, mock
from get_book_titles import GetBook
from inventory_client import RpcClient

mock_client = MagicMock()

dic = {"1":"B1", "2":"B2","3":"B3"}

def side_effect(*args):
    res = []
    isbn_list = args[1]
    for i in range(len(isbn_list)):
        res.append(dic[isbn_list[i]])
    return res

class Test_get_book_titles(TestCase):
    def test_contains(self):
        isbns = ["1","2"]
        target = ["B1","B2"]
        with mock.patch.object(GetBook, 'get_titles', side_effect=side_effect):
            res = GetBook.get_titles(mock_client, isbns)
            print("Return titles:")
            print(res)
            self.assertIsNotNone(res)
            self.assertListEqual(res, target)

if __name__ == "__main__":
    unittest.main()