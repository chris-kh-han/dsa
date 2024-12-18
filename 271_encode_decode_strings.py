def encode(strs: list[str]) -> str:
    res = ''
    for s in strs:
        res += str(len(s)) + '#' + s

    return res


def decode(s: str) -> list[str]:
    output = []
    i = 0
    while i < len(s):
        j = i
        if s[j] != '#':
            j += 1
        length = int(s[i:j])
        i = j + 1
        decoded = s[i: i+length]
        output.append(decoded)
        i += length
    return output


input = ["neet", "code", "love", "you"]

print(decode(encode(input)))

# Time Complexity:
# - encode: O(L) - we iterate through each character of each string once
# - decode: O(L) - we iterate through the encoded string once


# Space Complexity:
# - encode: O(L) - we store the encoded string which has length proportional to input
# - decode: O(L) - we store the decoded strings in output list
