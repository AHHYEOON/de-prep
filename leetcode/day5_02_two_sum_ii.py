"""
167. Two Sum II - Input Array Is Sorted
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Date: 2026-04-23

문제: 정렬된 배열에서 합이 target인 두 수의 인덱스 (1-indexed)

배운 것:
- 투포인터 패턴: 양 끝에서 시작 → 합 비교 → 조정
- 정렬된 배열의 조건 활용 → O(n) 시간 + O(1) 공간
- +=, -=로 변수 갱신 (Python에 ++, -- 없음)
- 1-indexed 주의 (return [left+1, right+1])
"""

from typing import List


class Solution:
    # 투포인터 - O(n) 시간, O(1) 공간
    # 배열이 정렬되어 있다는 조건을 활용
    # 합이 크면 right--, 작으면 left++
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1