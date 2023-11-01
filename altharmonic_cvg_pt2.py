import numpy as np
from math import e

cvgValue = 6
numOfPasses = 100


def print_partial_sum_and_terms(partial_sum, k, series_type):
    print(f"{series_type} {k} terms to reach partial sum {partial_sum}")


def convergeHarmonic(TARGET, num_passes=5):
    def converge_to_target(TARGET, series_type, term_count):
        partial_sum = 0
        k = 0

        while k < term_count:
            k += 1
            partial_sum += 1 / (2 * k - (1 if series_type == 'odd' else 0))

        TARGET = partial_sum - TARGET
        print_partial_sum_and_terms(
            partial_sum, k, f"added {k} {series_type} series terms")

        return TARGET

    for i in range(num_passes):
        term_count = i + 1  # Increase the term count with each pass
        TARGET = converge_to_target(
            TARGET, 'odd' if i % 2 == 0 else 'even', term_count)


# Example usage with a target of 2.5 and 5 passes
convergeHarmonic(cvgValue, numOfPasses)
