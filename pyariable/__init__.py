
class ValidationError(Exception):
    pass


class Variable:
    def __init__(self, is_valid=None):
        self.is_valid = is_valid

    def __eq__(self, b: object) -> bool:
        try:
            return self.value == b
        except AttributeError:
            if self.is_valid:
                if not self.is_valid(b):
                    raise ValidationError(b)
            self.value: object = b
            return True

    def __lt__(self, b) -> bool:
        try:
            return self.value < b
        except AttributeError:
            raise Exception("Unknown value")

    def __le__(self, b) -> bool:
        try:
            return self.value <= b
        except AttributeError:
            raise Exception("Unknown value")

    def __gt__(self, b) -> bool:
        try:
            return self.value > b
        except AttributeError:
            raise Exception("Unknown value")

    def __ge__(self, b) -> bool:
        try:
            return self.value >= b
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


class UniversalVariable:
    def __init__(self, is_valid=None):
        self.is_valid = is_valid

    def __eq__(self, b: object) -> bool:
        if self.is_valid:
            if not self.is_valid(b):
                raise ValidationError(b)
        return True


def variables(n):
    for _ in range(n):
        yield Variable()
