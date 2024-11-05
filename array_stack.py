from typing import List


def merge(nums1, m, nums2, n):
    '''
    # Example usage
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    Output should be [1, 2, 2, 3, 5, 6]
    '''

    p1 = m-1
    p2 = n-1 
    p = m+n-1

    while p2 >= 0 :
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1 
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1


# helloworld, 3 
'''
1 h   o   l
2 e l w r d
3 l   o

holelwrdlo

char = helloworld
nums = 3-  0, 1, 2
step = 1 for downward and -1 for upward
[
0 ['h', 'o', 'l']
1 ['e', 'l', 'w', 'r', 'd']
2 ['l', 'o']
]
'''
def zigzag_conversion(self, s, numrows):

    if numrows == 1 or numrows >= len(s):
        return s
    
    row = [[] for row in range(numrows)]
    index = 0
    step = 1 

    for char in s :
        row[index].append(char)
        if index == 0:
            step = 1
        elif index == numrows - 1:
            step = -1
        index += step

    for i in range(numrows):
        row[i] = ''.join(row[i])
    return ''.join(row)


''''
the sky is blue -> blue is sky the 
left       right

swap the words 

blue sky is the
blue is sky the 
'''
def reverse_string(self, s):

    words = s.split()
    left, right = 0, len(words)-1

    while left < right :
        words[left] , words[right] = words[right], words[left]
        left += 1
        right -= 1

    return " ".join(words)

'''
[1,2,3,4,5,6] and k = 3, rotate 3 times towards right 

[6,1,2,3,4,5] -> [5,6,1,2,3,4] -> [4,5,6,1,2,3]
Sol
[6,5,4,3,2,1] split by k [6,5,4] and [3,2,1] reverse this 
'''
def rotate_array( nums, k):
     print("Before Rotating Arrray", nums)
     l, r = 0, len(nums)-1
     k = k % len(nums) # give 3
     print(k)

     while l < r:
         nums[l], nums[r] = nums[r], nums[l]
         l, r = l+1, r-1

     l, r = 0, k-1
     while l < r:
      nums[l], nums[r] = nums[r], nums[l]
      l, r = l+1, r-1

     l, r = k, len(nums)-1
     while l < r:
         nums[l], nums[r] = nums[r], nums[l]
         l, r = l+1, r-1
    
     print("Rotate Array", nums)

'''
Can complete or not 
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
 gas - [1,2,3,4,5]
 cost - [3,4,5,1,2]
 diff - [-2, -2,-2, 3,3]
 if it is negative it won't work , in general the one with positive is good. 
 so index 3


Input: gas = [2,3,4], cost = [3,4,3]
Output: -1

SUM(gas) >= sum(cost) else -1 
don't have enough gas to complete the cost
also
'''
def gas_station(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    
    total = 0
    start = 0

    for i in range(len(gas)):
        total += ( gas[i] - cost[i] )
        # if total diff is leff than 0 they its not a soln
        # reset total to 0 and increase the index
        if total < 0:
            total = 0
            start = i+1
    return start


'''
[1, 4, 5, 8, 12], target = 6
answers is [1,3]
'''
def twosum(nums, target):
    l, r = 0, len(nums)-1

    while l < r:
        total = nums[l] + nums[r]
        if total == target:
            return [l+1, r+1]
        elif total > target:
            r -= 1 
        else:
            l += 1


'''
noon 

'''
def palindrome(s):
    l = 0
    r = len(s)-1
    while l < r:
        # this is for string palindrome
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        elif s[l] == s[r]:
            l += 1
            r -= 1
        else:
            False
    return True


'''
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 
'''

def rain_water(heights):
    l, r = 0, len(heights)-1
    max_area = 0

    while l < r:
        area = (r-l) * min(heights[r], heights[l])

        max_area = max(area, max_area) 
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    return max_area


'''
three sum 
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

First sort it 
[i, i+1, i+2]
[-3, -3, 0, 0, 1, 2] ( nlogn)
a = -3 and then 2 sum problem
'''

def threesum(nums):

    res = []
    nums.sort() #sort the array first 

    # we need to have atleast one on left or on right so we take -2  not -1
    for i in range(len(nums)-2):

        #skip if tge same element to avoid duplicates triplets
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i+1, len(nums)-1

        while left < right: 
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                
                # skip duplicates for the left pointer 
                while left < right and nums[left] == nums[left-1]:
                    left += 1

                # skip duplicates for the right pointer
                while left < right and nums[right] == nums[right+1]:
                    right -= 1


            elif total < 0:
                left += 1
            else :
                right -= 1
        return res 

'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from 
the original string by deleting some (can be none) of the characters 
without disturbing the relative positions of the remaining characters.
 (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 2 pointers or dynamic problem

 abc  ahgbiuc
 i    j
'''

def subsequence( s, t):

    i , j = 0,0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            #increse both of them
            i += 1
            j += 1
        else:
            #not found increase j to check other characters 
            j += 1
    
    # if one of element is not found in t from s, it would stop 
    # saying we don't find the number 
    return True if i == len(s) else False


'''
Given an integer array nums sorted in non-decreasing order, remove
 the duplicates in-place such that each unique element appears
 only once. The relative order of the elements should be kept the same.
   Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get
 accepted, you need to do the following things:

Change the array nums such that the first k elements of
 nums contain the unique elements in the order they were present in
   nums initially. The remaining elements of nums are not important 
   as well as the size of nums.
Return k.

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

[1,1,2]
   L
   R R R
Two pointers are used, Left to update the inplace and right to move  

'''    
def remove_duplicate(s):

    left = 1

    for right in range(1,len(s)):
        # current and previous is not same
        if s[right] != s[right -1]:
            #replace at the left index
            s[left] = s[right]
            left += 1
            #right += 1 this is not required as for loop does it 
    return left



def remove_duplicate_2 ( s):

    l, r = 0,0

    while r < len(s):
        count = 1 #should not be more than 2 
        while s[r] == s[r+1]:
            count += 1
            r += 1
        
        for i in range(min(2, count)):
            s[l] = s[r]
        r += 1
    
    return l 

    


if __name__ == "__main__":
    a = [1,2,3,0,0,0]
    m = 3
    b = [2,5,6]
    n = 3
    merge(a, m, b, n)
    print("Merge", a)

    nums = [1,2,3,4,5,6]
    rotate_array(nums, 3)

    print("=======================\n")
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]

    res = gas_station(gas,cost)
    print(res)

        
