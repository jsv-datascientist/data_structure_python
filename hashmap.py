
from collections import defaultdict
from typing import Counter, List


class Solution:

    '''
     s = anagram , t = nagrama

     hasts 

     a 3
     n 1
     g 1

    '''
    def valid_anagram(self, s:str, t:str) -> bool :
        #return sorted(s) = sorted(t)

        #return Counter(s) == Counter(t)
    
        if len(s) != len(t):
            return False 
        
        #create hash map in python
        countS , countT ={}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # this is same as count[s[i]], but if not found it should not crash 
            countT[t[i]] = 1 + countT.get(t[i], 0)

        #iterate the hashmap using Key
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        
        return True


''''
Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

time O(m * nlogn) and space is O(m * n )
'''

def group_anagram(self, str : List[str]) -> List[List[str]]:
    from collections import defaultdict

    anagram = defaultdict(list)  # the values will be list 
    for word in str:
        sorted_word = "".join(sorted(word))

        # "aet" : [eat, ate, tea]
        anagram[sorted_word].append(word)

    return list(anagram.values())


'''
nums = [100, 4, 200, 1, 3, 2]

Find the beginning of the sequence 

1,2,3,4  100, 200

Objectibe - Sort it and find the start of sequence 
check on left if has it is not the start of sequence  100 ( does it has 99 ? no , so its start of sequence)

'''

def longestConsecutive(self, nums : List[int]) -> int:
     # Create a set of numbers for O(1) lookup
    num_set = set(nums)

    longest_streak = 0

    for num in num_set:

        #check of left side any number is there
        if num-1 not in num_set:
            length = 0
            while (num+length) in num_set:
                length += 1
            longest = max(length, longest_streak)
    return longest_streak




if __name__ = "__main__":
