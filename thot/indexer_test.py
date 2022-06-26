import unittest
from indexer import Indexer
from term import Term

from tokenizer import Tokenizer

fake_docs = [
    { "id": 1, "text": "O rato roeu a roupa do rei de roma" },
    { "id": 2, "text": "O gato foi a roma" }
]

class TestIndexer(unittest.TestCase):

    def test_add_new_doc(self):
        terms = dict()
        tokenizer = Tokenizer('portuguese')
        indexer = Indexer(tokenizer)

        terms = indexer.add_doc(fake_docs[0], terms)
        terms = indexer.add_doc(fake_docs[1], terms)
        print(terms['rom'].references)

if __name__ == '__main__':
    unittest.main()
