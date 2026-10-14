class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #flatten matrix
        num_rows, num_columns = len(matrix), len(matrix[0])
        left, right = 0, num_rows*num_columns - 1


        while left <= right:
            middle = (left+right) // 2
            middleRow = middle // num_columns
            middleColumn = middle % num_columns

            if matrix[middleRow][middleColumn] == target:
                return True
            elif matrix[middleRow][middleColumn] < target:
                left = middle + 1
            else:
                right = middle - 1
        
        return False

            