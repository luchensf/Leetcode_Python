def maxArea(height):
    length = len(height)
    left = volume = 0
    right = length - 1
    while left < right:
        if height[left] > height[right]:
            area = height[right] * (right - left)
            if volume < area:
                volume = area
            right -= 1
        else:
            area = height[left] * (right - left)
            if volume < area:
                volume = area
            left += 1
    return volume