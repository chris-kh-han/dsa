def isPalindrome(s: str) -> bool:
    new_s = ''
    for char in s:

        if char.isalnum():
            new_s += char.lower()

    return new_s == new_s[::-1]


print(isPalindrome("tab a cat"))

# Use isalnum() method to remove non-alphanumeric characters
# Create variable new_s to store the lowercase string without whitespace
# Compare new_s with its reversed version
