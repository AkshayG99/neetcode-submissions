class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary search on rows
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            middle = (top+bottom)//2
            if matrix[middle][0] <= target <= matrix[middle][-1]:
                break
            if target < matrix[middle][0]:
                bottom = middle - 1
                continue
            top = middle + 1
        
        #binary search in a row
        left, right = 0, len(matrix[0]) - 1
        while left<=right:
            middle2 = (left+right)//2

            if matrix[middle][middle2] == target:
                return True

            if matrix[middle][middle2] < target:
                left = middle2+1
                continue

            right = middle2-1

        return False
