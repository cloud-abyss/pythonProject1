# 10000以内的完美数
# 完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和恰好等于它本身。

import math
for num in range(1, 10000):
    result = 0
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            result += factor
            if factor > 1 and num // factor != factor:
                result += num // factor
    if result == num:
        print(num)