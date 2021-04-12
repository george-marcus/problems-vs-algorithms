def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return None, None

    length_of_ints_list = len(ints)

    if length_of_ints_list == 0:
        return None, None

    # initialize min and max values with the first entry of the ints array
    min_value = ints[0]
    max_value = ints[0]

    # loop through range of integers starting from 1 to length of the array  minus 1
    for integer in range(1, length_of_ints_list):

        # change min value if the value of the ints[integer] is lower than the current min value
        if ints[integer] < min_value:
            min_value = ints[integer]
            continue

        # change max value if the value of the ints[integer] is larger than the current max value
        if ints[integer] > max_value:
            max_value = ints[integer]

    return min_value, max_value
