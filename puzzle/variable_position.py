# VariablePosition class - represents position of variable
class VariablePosition:
    def __init__(self, row_number: int, column_number: int):
        self.row_number: int = row_number
        self.column_number: int = column_number

    def __str__(self):
        return 'VariablePosition - row: {}, column: {}'.format(self.row_number, self.column_number)
