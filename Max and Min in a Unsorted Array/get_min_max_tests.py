import random
from get_min_max import get_min_max

# Example Test Case of Ten Integers

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("Pass" if ((None, None) == get_min_max([])) else "Fail")
print("Pass" if ((None, None) == get_min_max(None)) else "Fail")
print("Pass" if ((0, 0) == get_min_max([0])) else "Fail")
print("Pass" if ((0, 1) == get_min_max([0, 1])) else "Fail")
print("Pass" if ((0, 2) == get_min_max([0, 1, 1, 2])) else "Fail")
