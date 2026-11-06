class Solution:
    def trap(self, height: List[int]) -> int:
        p1, p2 = 0, 1
        area = 0
        tallestIdx = 1

        while p2 < len(height):
            while p2 < len(height) and height[p2] < height[p1]:
                if height[p2] > height[tallestIdx]:
                    tallestIdx = p2
                p2 += 1
            
            if p2 == len(height):
                p2 = tallestIdx
            # calculate area
            minHeight = min(height[p1], height[p2])
            for i in range(p1+1,p2):
                area += 0 if (minHeight-height[i]) <= 0 else (minHeight-height[i])

            p1=p2
            p2+=1
            tallestIdx = p2
        
        return area