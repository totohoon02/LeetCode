class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        y, x = 0, 0
        rows, cols = len(matrix), len(matrix[0])

        while True:
            is_all_empty = True
            for i in range(rows):
                if matrix[i]:
                    is_all_empty = False
                    mid_idx = len(matrix[i]) // 2
                    if matrix[i][mid_idx] > target:
                        matrix[i] = matrix[i][:mid_idx]
                    elif matrix[i][mid_idx] < target:
                        matrix[i] = matrix[i][mid_idx + 1:]
                    else:
                        return True

            if is_all_empty:
                return False