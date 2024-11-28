class TimeMap:

    def __init__(self):
        self.keyMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyMap:
            self.keyMap[key] = []
        self.keyMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.keyMap.get(key, [])
        res = ""
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return res


def main():
    timeMap = TimeMap()

    timeMap.set("foo", "bar", 1)
    print(timeMap.get("foo", 1))  # return "bar"
    print(timeMap.get("foo", 3))  # return "bar"
    timeMap.set("foo", "bar2", 4)
    print(timeMap.get("foo", 4))  # return "bar2"
    print(timeMap.get("foo", 5))  # return "bar2"


if __name__ == "__main__":
    main()

# Initialize the keyMap as dict and set the keyMap[key] to a list of [value, timestamp] ex key = "foo" => keyMap["foo"] = [["bar", 1], ["bar2", 4]]
# In the get method, use binary search to find the value that has timestamp <= given timestamp
# If the timestamp is found, update the result to the value
# Time complexity: O(logN)
# Space complexity: O(N) where N is the number of values for the given key
