class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix) < 1 or len(matrix[0]) < 1:
            return False

        row, col = 0, len(matrix[0]) - 1
        while col >= 0 and row <= len(matrix) - 1:
            if target == matrix[row][col]:
                return True
            if target < matrix[row][col]:
                col -= 1
            else:
                row += 1
        return False
