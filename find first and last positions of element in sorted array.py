class Solution:
    def searchRange(self, nums, target):
        def find_bound(is_first):
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    bound = mid
                    if is_first:
                        right = mid - 1  # move left to find first
                    else:
                        left = mid + 1   # move right to find last
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return bound
        
        first = find_bound(True)
        last = find_bound(False)
        return [first, last]
