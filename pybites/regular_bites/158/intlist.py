class IntList(list):
    def __init__(self, values):
        super().__init__(self._check_value(value) for value in values)

    def append(self, value):
        super().append(self._check_value(value))

    def __add__(self, other):
        new_values = [self._check_value(value) for value in other]
        return IntList(super().__add__(new_values))

    def __iadd__(self, other):
        new_values = [self._check_value(value) for value in other]
        return IntList(super().__iadd__(new_values))

    def _check_value(self, value):
        try:
            return int(value)
        except ValueError:
            raise TypeError("IntList only accepts integers")

    @property
    def mean(self):
        return sum(self) / len(self)

    @property
    def median(self):
        values = sorted(self)
        if len(values) % 2 == 0:
            return (values[len(values) // 2] + values[len(values) // 2 - 1]) / 2
        return values[len(values) // 2]
