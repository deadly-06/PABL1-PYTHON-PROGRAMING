class Solution:
    def groupAnagrams(self, strs):
        from collections import defaultdict
        
        anagrams = defaultdict(list)
        
        for word in strs:
            # Sort the word to form the key
            key = ''.join(sorted(word))
            anagrams[key].append(word)
        
        return list(anagrams.values())
