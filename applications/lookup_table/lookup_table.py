# Your code here
import math
import random


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


power_cache = {}
factorial_cache = {}
division_cache = {}
module_cache = {}


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here

    i = (x, y)
    v = None

    if i in power_cache:
        v = power_cache[i]
    else:
        power_cache[i] = math.pow(x, y)
        v = power_cache[i]

    if i in factorial_cache:
        v = factorial_cache[i]
    else:
        factorial_cache[i] = math.factorial(v)

    if i in division_cache:
        v = division_cache[i]
    else:
        division_cache[i] = v // (x + y)
        v = division_cache[i]

    if i in module_cache:
        v = module_cache[i]
    else:
        module_cache[i] = v % 982451653
        v = module_cache[i]
    return v


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
