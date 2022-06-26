import nltk

class Tokenizer:
    def __init__(self, language) -> None:
        self.__stop_words = nltk.corpus.stopwords.words(language)

    def __is_valid_token(self, token):
        return token not in self.__stop_words and token.isalpha()

    def __stemmize_token(self, token):
        stemmer = nltk.stem.RSLPStemmer()
        return stemmer.stem(token)

    def tokenize(self, text):
        tokens = []
        for token in nltk.word_tokenize(text):
            if self.__is_valid_token(token):
                lower_token = token.lower()
                stem_token = self.__stemmize_token(lower_token)
                tokens.append(stem_token)

        return tokens



