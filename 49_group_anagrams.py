def groupAnagrams(strs: list[str]) -> list[list[str]]:
    res = {}

    for str in strs:
        count = [0] * 26
        for c in str:
            count[ord(c) - ord('a')] += 1
        key = tuple(count)
        if key not in res:
            res[key] = []
        res[key].append(str)

    return list(res.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))


# Space Complexity: O(m * n), where m is the number of strings and n is the maximum length of each string
# Time Complexity: O(m * n), where m is the number of strings and n is the maximum length of each string, res dict
