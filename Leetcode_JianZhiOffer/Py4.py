class Solution:

    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:

        if matrix == [[]]:
            return False
        for i in matrix:
            if target > i[len(i) - 1]:
                continue
            for j in i:
                if target < i[0]:
                    continue
                if j == target:
                    return True
        return False

        # i, j = len(matrix) - 1, 0
        # while i >= 0 and j < len(matrix[0]):
        #     if matrix[i][j] > target: i -= 1
        #     elif matrix[i][j] < target: j += 1
        #     else: return True
        # return False