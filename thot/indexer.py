from typing import Callable, Dict, List
from term import Term
from tokenizer import Tokenizer

class Indexer:
    def __init__(self, tokenizer: Tokenizer) -> None:
        self.__tokenizer = tokenizer

    def add_doc(
        self,
        doc: Dict,
        terms: Dict[str, Term] = dict(),
        fields: List[str] = ['text'],
        reference_field = 'id'):

        tokens = []
        document_reference = doc[reference_field]

        for field in fields:
            current_tokens = self.__tokenizer.tokenize(doc[field])
            tokens += current_tokens

        for token in tokens:
            if token in terms:
                terms[token].add_reference(document_reference)
            else:
                terms[token] = Term(token, [document_reference])

        return terms

