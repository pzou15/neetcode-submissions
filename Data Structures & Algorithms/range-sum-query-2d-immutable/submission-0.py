class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixSums = []
        # theory: you can technically get the box bounded by the current row, col by adding up sequentially the row and including the
        # sum in the row above it to account for previous rows?
        for i in range(len(matrix)):
            row = []
            rowTotal = 0
            boxTotal = 0
            for j in range(len(matrix[0])):
                rowTotal += matrix[i][j]
                boxTotal = rowTotal + self.prefixSums[i-1][j] if i - 1 >= 0 else rowTotal # add sum of previous row
                row.append(boxTotal)
            self.prefixSums.append(row)
        print(self.prefixSums)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # remove danging col on the left if necessary
        total = self.prefixSums[row2][col2] - self.prefixSums[row2][col1-1] if col1 - 1 >= 0 else self.prefixSums[row2][col2]
        # remove rows above(?) region if necessary
        # NOTE: readd box that is defined by upper left corner (row1-1, col1-1) because it has overlap in 2 regions being removed
        
        if row1 - 1 >= 0:
            total -= self.prefixSums[row1-1][col2]
            total += self.prefixSums[row1-1][col1-1] if col1 - 1 >= 0 else 0

        return total

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)