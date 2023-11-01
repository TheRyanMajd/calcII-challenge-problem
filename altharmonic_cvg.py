import numpy as np
from math import e

cvgValue = 6


def convergeHarmonic(TARGET):
    def converge_to_target(TARGET, series_type):
        partial_sum = 0
        k = 0

        while partial_sum < TARGET:
            k += 1
            partial_sum += 1 / (2 * k - (1 if series_type == 'odd' else 0))

        TARGET = partial_sum - TARGET
        print(
            f"added {k} {series_type} series terms to reach partial sum {partial_sum}")

        return TARGET

    TARGET = converge_to_target(TARGET, 'odd')
    TARGET = converge_to_target(TARGET, 'even')
    TARGET = converge_to_target(TARGET, 'odd')
    TARGET = converge_to_target(TARGET, 'even')
    TARGET = converge_to_target(TARGET, 'odd')


# Example usage with a target of 6
convergeHarmonic(cvgValue)
