"""
217. Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/
Date: 2026-04-22

문제: 배열에 중복이 있으면 True, 모두 고유하면 False

3가지 풀이 + 원라이너 비교

배운 것:
- set()은 값 존재 확인이 O(1)
- 정렬하면 중복은 이웃이 됨 -> 옆 값만 비교하면 O(nlogn)
- 이중 for문에서 range(i+1, ...) 로 최적화
- return 문 들여쓰기 = 스코프 결정 (Python에서 주의)
"""

from typing import List


class Solution:
    # 풀이 1: 완전 탐색 - O(n²)
    # - 이중 for문으로 모든 쌍 비교
    # - range(i+1, n)으로 뒷부분만 검사 (최적화)
    def containsDuplicate_bruteforce(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    
    # 풀이 2: 정렬 - O(nlogn)
    # - 정렬하면 중복은 반드시 이웃
    # - range(len(nums)-1)로 끝까지 비교해도 IndexError 방지
    def containsDuplicate_sort(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
    
    # 풀이 3: 해시셋 - O(n) (가장 좋음)
    # - 본 숫자를 set에 저장, 다시 나타나면 True
    # - in 연산이 O(1)이라 가장 빠름
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
    # 풀이 4 (보너스): 원라이너 - O(n)
    # - set()으로 변환해 중복 제거 후 길이 비교
    # - Pythonic하지만 사고 과정이 덜 드러남
    def containsDuplicate_oneline(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))