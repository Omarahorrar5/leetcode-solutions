class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        max_area = (right-left) * min(height[left], height[right])
        while left < right:
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
            area = (right-left) * min(height[left], height[right])
            if area > max_area:
                max_area = area
        return max_area
            