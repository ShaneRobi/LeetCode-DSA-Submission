class Solution:
    def reverseVowels(self, s: str) -> str:
        letters = list(s)
        right = len(letters) - 1
        left = 0
        vowels = "aeiouAEIOU"
        while left < right:
            if letters[left] not in vowels:
                left = left + 1
            if letters[right] not in vowels:
                right = right -1
            if letters[left] in vowels and letters[right] in vowels:
                letters[left], letters[right] = letters[right], letters[left]
                left = left + 1
                right = right - 1
        return "".join(letters)

