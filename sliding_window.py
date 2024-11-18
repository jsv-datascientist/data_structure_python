class Solution:

    def __init__(self):
        pass

    '''
    Given an array of positive integers nums and a positive integer target, return the minimal length of a 
    subarray
    whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

    Example 1:

    Input: target = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: The subarray [4,3] has the minimal length under the problem constraint.
    '''
    
    def minSubArrayLen(self, target, nums):
        
        left = 0
        sum = 0
        min_length = float('inf')

        for right in range(len(nums)):

            sum += nums[right]

            while sum >= target :
                min_length = min(min_length, right-left+1)
                sum -= nums[left]
                left += 1
        
        return min_length if min_length != float('inf') else 0
        



    '''
    Given a string s, find the length of the longest 
    substring
    without repeating characters.

    Example 1:

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
    Example 2:

    '''
    def lengthOfLongestSubstring(self, s):
        left = 0
        max_length = 0
        hashmap = {}

        for right in range(len(s)):

            value = s[right]
            if value in hashmap:
                left = max(left,hashmap[value] + 1)


            hashmap[value] = right
            max_length = max(max_length, right-left+1)
        return max_length


if __name__ == "__main__":

    print("Minimim Size SubArray Sum \n")
    target = 7
    nums = [2,3,1,2,4,3]

    solution = Solution()
    print("Min sum array size is : ",solution.minSubArrayLen(target, nums) , end="\n")

    s = "abcabcbb"

    print("Longest subsequence is : ",solution.lengthOfLongestSubstring(s))