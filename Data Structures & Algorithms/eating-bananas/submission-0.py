import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = float('-inf')
        for pile in piles:
            right = max(right, pile)
        k = float('inf')

        while left <= right:
            middle = (left+right) // 2
            count = 0
            for pile in piles:
                count += math.ceil(pile/middle)
            if count <= h:
                k = min(k, middle)
                right = middle - 1
            if count > h:
                left = middle + 1
        
        return k
