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
        



if __name__ == "__main__":

    print("Minimim Size SubArray Sum \n")
    target = 7
    nums = [2,3,1,2,4,3]

    solution = Solution()
    print(solution.minSubArrayLen(target, nums))