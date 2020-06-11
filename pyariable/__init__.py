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

    def __round__(self, x):
        return round(self.value, x)

    def __int__(self):
        return int(self.value)


def variables(n):
    for _ in range(n):
        yield Variable()
