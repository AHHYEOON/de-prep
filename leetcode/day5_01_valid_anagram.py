"""
242. Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/
Date: 2026-04-23

문제: 두 문자열이 같은 글자 재배열인지 확인

배운 것:
- sorted()는 리스트 반환 (문자열이 아님!)
- dict.get(key, default) 패턴으로 딕셔너리 카운팅
- Early Return 3단계: 길이 비교 → 키 존재 확인 → 음수 체크
- Counter는 카운팅 전용 dict 서브클래스
"""

from typing import List
from collections import Counter


class Solution:
    # 풀이 1: 정렬 - O(n log n)
    # - sorted()로 문자열을 리스트로 정렬 후 비교
    # - 가장 간결하지만 정렬 비용 있음
    def isAnagram_sort(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
    # 풀이 2: 딕셔너리 카운팅 - O(n)
    # - Early Return으로 효율 극대화
    # - s에서 카운트 +1, t에서 카운트 -1, 음수면 불일치
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False
        
        return True
    
    # 풀이 3 : Counter - O(n)
    # - collections.Counter는 카운팅 전용 자료구조
    # - Pythonic하지만 내부 원리 이해가 중요
    def isAnagram_counter(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)