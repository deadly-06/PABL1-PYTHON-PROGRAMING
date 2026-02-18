class Solution:
    def subsets(self, nums):
        result = []
        
        def backtrack(index, path):
            # Add the current subset
            result.append(path[:])
            
            # Explore further elements
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()  # backtrack
        
        backtrack(0, [])
        return result
