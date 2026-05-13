class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right = len(heights) - 1
        left = 0
        
        best = 0
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)

                        
            best = max(area, best)
            if heights[left] <= heights[right]:
                left+= 1
            elif heights[left] > heights[right]:
                right -= 1
                     
        return best    


        