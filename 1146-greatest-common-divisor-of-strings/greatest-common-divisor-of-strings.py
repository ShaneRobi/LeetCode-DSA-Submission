import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        candidate_len = math.gcd(len(str1), len(str2)) # this is to have the length of the candidates. using "len(str)" <-- to measure the length of the strings. variable is named candidate_len.
        candidate = str1[:candidate_len]
        if candidate * (len(str1) // candidate_len) == str1:
            if candidate * (len(str2) // candidate_len) == str2:
                return candidate
        return ""
        
