class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row
        targetRow = -1
        bottom, top = 0, len(matrix) - 1
        if len(matrix) == 1:
            targetRow = 0
        else:
            while bottom <= top:
                middle = (bottom + top) // 2

                if matrix[middle][0] <= target <= matrix[middle][-1]:
                    targetRow = middle
                    break
                elif matrix[middle][0] < target:
                    bottom = middle + 1
                else:
                    top = middle - 1
        
        if targetRow == -1:
            return False
        
        left, right = 0, len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[targetRow][mid] == target:
                return True
            elif matrix[targetRow][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False


