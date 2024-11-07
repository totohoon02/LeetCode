class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            water = (right - left) * min(height[left], height[right])
            
            maximum = max(water, maximum)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return maximum