import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            middle = (left+right) // 2
            count = 0
            for pile in piles:
                count += (pile + middle - 1) // middle
            if count <= h:
                right = middle - 1
            if count > h:
                left = middle + 1
        
        return left
