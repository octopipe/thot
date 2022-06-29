from tokenizer import Tokenizer

class SimpleQueryParser:
    def __init__(self, tokenizer: Tokenizer) -> None:
        self.tokenizer = tokenizer

    def parse(self, query):
        tokens = self.tokenizer.tokenize(query)
        return tokens

