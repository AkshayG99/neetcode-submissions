class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        bottom, top = 0, len(matrix) - 1
        row = None

        while bottom <= top:
            middle = (bottom + top) // 2

            if matrix[middle][0] <= target <= matrix[middle][-1]:
                row = middle
                break
            elif matrix[middle][0] > target:
                top = middle - 1
                #middle[0] < target
            else:
                bottom = middle + 1
        
        if row == None:
            return False
        
        left, right = 0, len(matrix[0]) - 1

        while left <= right:
            middle = (left + right) // 2

            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        
        return False