class Variable:
    def __eq__(self, b: object) -> bool:
        try:
            return self.value == b
        except AttributeError:
            self.value: object = b
            return True

    def __lt__(self, b) -> bool:
        try:
            return self.value < b
        except AttributeError:
            raise Exception("Unknown value")

    def __gt__(self, b) -> bool:
        try:
            return self.value > b
        except AttributeError:
            raise Exception("Unknown value")

    def __repr__(self) -> str:
        try:
            return repr(self.value)
        except AttributeError:
            return "?"
