class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        
        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # If number is too large, stop early
                if candidates[i] > remaining:
                    break
                
                path.append(candidates[i])
                
                # Move to next index (i + 1) since we can't reuse same number
                backtrack(i + 1, path, remaining - candidates[i])
                
                path.pop()
        
        backtrack(0, [], target)
        return result
