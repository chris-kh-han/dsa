def validPalindrome(self, s: str) -> bool:
    def is_palindrome(l: int, r: int) -> bool:

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
        left += 1
        right -= 1

    return True

print(validPalindrome("aba"))
print(validPalindrome("abca"))
print(validPalindrome("abc"))

# used two pointer approach
# time complexity will be O(n) maximum will be twice the length of string
# space complexity will be O(1) no extra space is used
