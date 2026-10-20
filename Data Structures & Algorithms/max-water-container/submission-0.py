class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right = 0
        left = len(heights) - 1

        maxVol = 0

        while(right < left):
            maxHeight = min(heights[right], heights[left])
            vol = (left - right) * maxHeight
            
            maxVol = max(vol, maxVol)

            if heights[right] < heights[left]:
                right += 1
            else:
                left -= 1

        return maxVol


#we also think that when right<= left which means the area is technically zero which is not what we are calculating

# also think of the part when we are shinkring

        