import uuid
from typing import Callable, Dict, List
from term import Term
from tokenizer import Tokenizer

class Indexer:
    def __init__(self, tokenizer: Tokenizer) -> None:
        self.__tokenizer = tokenizer

    def add_doc(
        self,
        doc: Dict,
        index_fields: List[str],
        save_field: str,
        terms: Dict[str, Term] = dict()):

        tokens = []
        document_id = uuid.uuid4()

        for field in index_fields:
            current_tokens = self.__tokenizer.tokenize(doc[field])
            tokens += current_tokens

        for token in tokens:
            if token in terms:
                terms[token].add_reference(document_id)
            else:
                terms[token] = Term(token, [document_id])

        return terms

