class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK, maxK = 1, max(piles)
    
        while minK <= maxK:
            middleK = (minK + maxK) // 2
            counter=0

            for i in range(len(piles)):
                counter += (piles[i] + middleK - 1 ) // middleK
                
            if (counter <= h):
                maxK = middleK - 1
            else:
                minK = middleK + 1
        
        return minK
