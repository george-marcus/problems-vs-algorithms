def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if input_list is None:
        return None

    if len(input_list) == 0:
        return []

    start_index = 0
    last_index = len(input_list) - 1

    # index to keep track of all zero values as we only have 0,1 or 2 in out input array
    matched_zeros_count = 0

    # we will compare each list element against 0,1, or 2
    while start_index <= last_index:

        if input_list[start_index] == 0:

            # swap value of start index with the last matched index of a zero value
            input_list[start_index] = input_list[matched_zeros_count]

            # now the value at the matched index of zeros count should be zero
            input_list[matched_zeros_count] = 0

            # increment start index
            start_index += 1

            # increment matched zeros
            matched_zeros_count += 1

            continue

        if input_list[start_index] == 1:
            # just increment start index as value 1 should be in the middle of the array
            start_index += 1
            continue

        if input_list[start_index] == 2:
            # swap start index's value with last index's value
            input_list[start_index] = input_list[last_index]

            # value of the last index should be 2
            input_list[last_index] = 2

            # decrement last index as we won't need it again it has its final value 2
            last_index -= 1

    return input_list
