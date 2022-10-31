class Matrix:
    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'

    # Courtesy of https://geekflare.com/multiply-matrices-in-python/
    # Had to find this, never done this in any math class before.
    def __matmul__(self, other):
        return Matrix(
            [
                [
                    sum(a * b for a, b in zip(A_row, B_col))
                    for B_col in zip(*other.values)
                ]
                for A_row in self.values
            ]
        )

    def __rmatmul__(self, other):
        return self.__matmul__(other)

    def __imatmul__(self, other):
        self.values = self.__matmul__(other).values
        return self
