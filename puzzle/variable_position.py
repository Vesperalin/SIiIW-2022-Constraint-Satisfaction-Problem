class VariablePosition:
    def __init__(self, row_number, column_number):
        self.row_number = row_number
        self.column_number = column_number

    def __str__(self):
        return 'Position - row: {}, column: {}'.format(self.row_number, self.column_number)
