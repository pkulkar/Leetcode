"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""

"""
Time Complexity: O(n)
Space Complexity O(n)
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        return self.rob_recursion(nums, len(nums)-1, memo)
    
    def rob_recursion(self, nums, i, memo):
        if i < 0:
            return 0
        if memo[i] >= 0:
            return memo[i]
        taken = nums[i] + self.rob_recursion(nums, i-2, memo)
        not_taken = self.rob_recursion(nums, i-1, memo)
        max_loot = max(taken, not_taken)
        memo[i] = max_loot
        return max_loot

"""
Time Complexity: O(n)
Space Complexity O(1)
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_max = 0
        curr_max = 0
        for i in range(len(nums)):
            temp = curr_max
            curr_max = max(prev_max + nums[i], curr_max)
            prev_max = temp
        return curr_max
