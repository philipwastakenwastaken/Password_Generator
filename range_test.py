import random;
import functools


def randomPicker(howMany, *ranges):
    print(ranges)
    for x in ranges:
        mergedRange += x
    ans = []
    for i in range(howMany):
        ans.append(random.choice(mergedRange))
    return ans


print(randomPicker(5, range(15, 20), range(36, 255)))
