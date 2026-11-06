class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen, colLen = len(matrix), len(matrix[0])
        l, r = 0, rowLen * colLen - 1 

        while l <= r:
            mid = (l + r)//2

            if matrix[mid // colLen][mid % colLen] == target:
                return True
            elif matrix[mid // colLen][mid % colLen] < target:
                l = mid + 1
            else:
                r = mid - 1 
        
        return False