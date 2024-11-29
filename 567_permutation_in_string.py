from collections import defaultdict


def checkInclusion(s1: str, s2: str) -> bool:
    dict1 = defaultdict(int)
    dict2 = defaultdict(int)

    l1 = len(s1)
    l2 = 0

    for char in s1:
        dict1[char] += 1

    for r in range(len(s2)):
        dict2[s2[r]] += 1

        if (r - l2 + 1) > l1:
            dict2[s2[l2]] -= 1
            if dict2[s2[l2]] == 0:
                del dict2[s2[l2]]
            l2 += 1

        if dict1 == dict2:
            return True

    return False


# The window size for s2 depends on the size of s1.
# If (r - l2 + 1) > l1, it means the window size of s2 is larger than that of s1.
# In this case, we need to move the window to the right by incrementing l2 by 1
# and remove characters when their count reaches 0.
# Dictionaries are considered equal only if their keys and values match exactly.
# If a key with a value of 0 remains in one dictionary, it can cause the comparison to fail,
# even though the additional key is meaningless.
# Example:
# dict1 = {'a': 1, 'b': 1}
# dict2 = {'a': 1, 'b': 1, 'c': 0}
# print(dict1 == dict2)  # Output: False (the extra 'c': 0 causes the comparison to fail)
# Time complexity is O(n), where n is the length of s2.
# Space complexity is O(len(s1)).
