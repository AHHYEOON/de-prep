"""
1. Two Sum
Link: https://leetcode.com/problems/two-sum/

문제: 합이 target이 되는 두 수의 인덱스 찾기
"""

from typing import List

class Solution:
    # 풀이 1: 완전 탐색 (Brute Force) - O(n²)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]
    
    # 풀이 2: 해시맵 (Dictionary) - O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i