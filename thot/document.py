class Document:
    def __init__(self, id: str) -> None:
        self.id = id
        self.fields = dict[str]()

