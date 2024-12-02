def plusOne(digits: list[int]) -> list[int]:
    for i in range(len(digits)-1, -1, -1):
        if digits[i] + 1 != 10:
            digits[i] += 1
            return digits

        digits[i] = 0

        if i == 0:
            return [1] + digits


digits = [9, 9]

print(plusOne(digits))

# Loop through the digits in reverse order and check if the digit is 9, which requires a carry.
# If the leftmost digit is 9, it will trigger the carry logic.
# Otherwise, simply increment the digit by 1 and return the result.
