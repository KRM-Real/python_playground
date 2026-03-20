# 49.Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]



from collections import defaultdict

def groupAnagrams(self, strs):
    anagram_map = defaultdict(list)
        
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
        
    return list(anagram_map.values())