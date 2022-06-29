from thot.indexer import Indexer
from thot.tokenizer import Tokenizer

fake_docs = [
    { "id": 1, "text": "Sabio é aquele que conhece os proprios limites da ignorancia" },
    { "id": 2, "text": "Penso logo existo" }
    { "id": 3, "text": "Acredite em milgares mas nao dependa deles" }
]

if __name__ == "__main__":
    tokenizer = Tokenizer('portuguese')
    indexer = Indexer(tokenizer)

    indexer(
