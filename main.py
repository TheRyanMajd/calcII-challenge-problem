import numpy as np
from math import e
ln2 = np.emath.logn(e, 2)
delta = ln2
isAlternative = False
m = 1  # m changes the amount of print statements made per additional term
CEIL = 10  # The highest number of terms that the print goes to


def summation(n):
    partial_sum = 0.0
    for i in range(1, n + 1):
        partial_sum += 1.0 / i
    return partial_sum

# not compeleted yet


def altSummation(n):
    partial_sum = 0.0
    for i in range(1, n + 1):
        if i % 2 == 1:
            partial_sum += 1.0 / i
        else:
            partial_sum -= 1.0 / i
    return partial_sum


for i in range(1, CEIL + 1):
    if (not isAlternative):
        result = summation(i)
        if i % m == 0:  # Print every 1000 terms for better readability
            print("Partial Harmonic Sum ({} terms): {:.10f}".format(i, result))
    elif isAlternative:
        result = altSummation(i)
        if i % m == 0:  # Print every 1000 terms for better readability
            # np.log(2, e)
            delta = abs(result - ln2)  # Calculate the absolute difference
        output = "Partial Alternative Harmonic Sum ({} terms): {:.10f}, ln(2): {:.7f}, Δ: {:.10f}".format(
            i, result, ln2, delta)
        print(output)
