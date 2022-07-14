# # codewars problems
# An anagram is the result of rearranging the letters of a word 
# to produce a new word (see wikipedia).

# Note: anagrams are case insensitive

# Complete the function to return true if the two arguments given are anagrams of each other; 
# return false otherwise.

# Examples
# "foefet" is an anagram of "toffee"

# "Buckethead" is an anagram of "DeathCubeK"

def is_anagram(test, orig):
    key = {}
    for t in test:
        if t in key:
            key[t] +=1
        else:
            key[t] = 1
    for o in orig:
        if o in key:
            key[o] -= 1
        else:
            return False
    for v in key.values():
        if v == 0:
            continue
        else:
            return False
    return True


# the above code run with 'return key' will return the amount of character in the key


print(is_anagram('toffee', 'foefet'))

# whiteboard of the day - Shoha
# Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers 
# such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# create a visited dict to store KEY: Number VAL: index
# iterate over our nums list
# if the pair is already inside of VISITED:
    # DONE. Return current index and the VAL from dict
# otherwise, simply add the number and the current position to dict

def twoSum(nums, target):
    visited = {}
    for i in range(len(nums)):
        num = nums[i]
        pair = target - num
        if pair in visited:
            return [visited[pair], i]
        visited[num] = i

    return []

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))

# spend time thinking about the code
# think out loud when doing technical questions/whiteboards
# start off reading out the problem
# make assumptions
# ask clarifying questions
# be particular about your data