class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            # Calculate current area
            width = right - left
            h = min(height[left], height[right])
            current_water = width * h
            
            # Update maximum water found
            if current_water > max_water:
                max_water = current_water

            # Move the pointer pointing to the shorter vertical line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water