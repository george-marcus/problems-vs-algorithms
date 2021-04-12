import sys
import math


def sqrt(number):
    """
    Calculate the floored square root of a number
    This is a divide and conquer algorithm

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number is None or not isinstance(number, int):
        return None

    # Square root of absolute values 1 and 0 are the same as the original values
    if abs(number) == 1 or abs(number) == 0:
        return number

    negligible_approximation = 0.01

    mid = number/2

    lower_bound = 0
    upper_bound = number

    while abs(mid**2 - number) >= negligible_approximation:

        # determine which bound our mid value is close to
        if mid**2 < number:
            lower_bound = mid
        else:
            upper_bound = mid

        # combine upper and lower bound and divide them by half to repeat the cycle
        mid = (lower_bound + upper_bound)/2

    # get the rounded value of the mid
    return math.floor(mid)
