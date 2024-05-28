from collections import defaultdict
import math
import typing


def say_hello():
    print("Hello Python my (old) new friend!")

    # Types are optional, infact don't use it unless required
    a = "some str"  # No need to declare that a is str
    a = 19  # Reassign to different type works
    n: int = -11

    f: float = 10.0
    f = (int)(f)  # Type casting (int) is equivalent to int(f)
    print(f)
    f: float = 10.0
    f = int(f)  # Type casting (int) is equivalent to int(f)
    print(f)
    print(n / f)  # Division always returns float
    print(n // f)  # special operator called integer division, returns int
    # // Operator has different behavior in python for negative numbers, it returns floor value
    print(
        math.floor(n / f)
    )  # Floor function can be used to get same behavior as // operator
    print(int(n / f))  # Type casting to int returns as expected from other languages
    b: bool = True
    s: str = "abcd"
    a = s  # No warning
    n = s  # Warning?
    n1 = n2 = n3 = 110  # Multiple declaration
    n = 10
    print(n1)
    pair = (n, f)  # Declare tuple like this
    pairT: tuple[int, float] = (3, 4.2)  # Declare with typedef
    print(type(pair), pair)

    m = {}  # Declare a map
    # Python data structures can be heterogeneous
    # Wild west
    m[30] = 1
    m["st"] = None
    m[3.2] = "really"

    print(m)

    print("LISTS")
    # Lists are arrays
    arr = [1, 2, 4.0, "str", True]
    arr.append(a)
    print(arr)

    # List slicing
    print(arr[1:3])  # 1 inclusive, 3 exclusive
    print(arr[1:])  # 1 inclusive, till end
    print(arr[:3])  # 0 inclusive, 3 exclusive
    print(arr[:-1])  # 0 inclusive, -1 exclusive (last element)
    print(arr[-1:])  # -1 inclusive (last element), till end, i.e. last element only

    # No traditional loop for(int = 0; i < n; i++) in python
    # Alternatives
    # 1. Using range function (requires int as parameter)
    for i in range(len(arr)):
        print(arr[i])

    # 2. using enumerate with value
    for i, v in enumerate(arr):
        print(i, v)

    # 3. If you dont need index
    for v in arr:
        print(v)

    # 4. Strings are also list of 1-length str (hereby called char by me), so same things work for strings as well
    for c in s:
        print(c)

    for i, c in enumerate(s):
        print(i, c)

    for i in range(len(s)):
        print(i, s[i])

    # Convert char to int value
    for c in s:
        print(ord(c) - ord("a"))

    # Convert int to char value
    for i in range(26):
        print(chr(i + ord("a")))

    # Sort won't work on arrays of mixed types, can provide custom sorting function
    arr = [(1, 2), (5, 2), (2, 1), (1, 12), (11, 1), (5, 2)]
    arr.sort(
        key=get_second_val,
    )
    print(arr)

    # Equivalent lambda
    arr = [(1, 2), (5, 2), (2, 1), (1, 12), (11, 1), (5, 2)]
    arr.sort(
        key=lambda t: t[-1],
    )
    print(arr)

    # default dict can be used with a default value for missing keys
    dm = defaultdict(lambda: "Missing")
    print("Key: ", dm["missing"])

    # default dict with 0 values
    dm = defaultdict(int)
    print("Not here: ", dm["somekey"])

    print(dm)

    # Mutable objects are pass by reference & immutable objects are pass by value
    n = 3
    double_this(n)
    print(n)  # Unchanged

    n = [3, 2]
    double_this(n)
    print(n)  # Array is mutable and gets updated


# Function definition like this
# No need to specify return value, although can do like this
def get_second_val(e) -> int:
    return e[-1]


def double_this(n):
    n *= 2


# Stacks
# Python lists can be used as stacks, with append and pop
def stack_example():
    stack = []
    stack.append(1)
    stack.append(2)
    stack.append(3)
    # Peek
    print(stack[-1])
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    # Check if stack is empty
    print(not stack)
    # Try to pop stack
    print(stack.pop() if stack else "Empty stack")


# Path: main.py
if __name__ == "__main__":
    say_hello()
