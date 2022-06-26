class Term:
    def __init__(self, token, references = [], cost = 0) -> None:
        self.token = token
        self.references = references
        self.cost = cost

    def add_reference(self, new_reference):
        self.references.append(new_reference)
