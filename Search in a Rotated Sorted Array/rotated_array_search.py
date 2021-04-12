def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    # returns -1 when list is empty or number value is not an integer
    if not input_list or not isinstance(number, int):
        return -1

    input_list_length = len(input_list)
    mid_index = (input_list_length - 1) // 2

    start_index = 0
    last_index = input_list_length - 1

    while start_index <= last_index:

        # we start from the middle value to narrow our search
        middle_value = input_list[mid_index]

        # bingo we're lucky the middle value is the one we're looking for
        if middle_value == number:
            return mid_index

        # or it could be the first value
        if input_list[start_index] == number:
            return start_index

        # or the last value
        if input_list[last_index] == number:
            return last_index

        #  increment strat index if number is smaller than values of start or last index
        if number < input_list[start_index] or number < input_list[last_index]:
            start_index = mid_index + 1

        # or decrement last index otherwise
        else:
            last_index = mid_index - 1

        # calculate the new midindex
        mid_index = (last_index - start_index) // 2

    return -1
