def lengthOfLongestSubstring(s: str) -> int:
    longest = 0
    sett = set()
    l = 0

    for r in range(len(s)):
        while s[r] in sett:
            sett.remove(s[l])
            l += 1

        sett.add(s[r])
        longest = max(longest, r - l + 1)

    return longest


s = 'abba'
s = 'pwwkew'
print(lengthOfLongestSubstring('pwwkew'))

# Space O(n) Time O(n)
# r-1+1 to get the length between two pointers
