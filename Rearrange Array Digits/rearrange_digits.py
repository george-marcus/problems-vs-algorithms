def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two digit such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # We assume that all input list elements are in the range [0, 9].

    input_list_length = len(input_list)

    if input_list_length == 0:
        return None

    digit_occurrence_count_dict = {
        digit: 1 if digit in input_list else 0 for digit in range(10)}

    # sort input_list digits by looping through the numbers from 0 to 9 in order
    #  if a number is in the occurence dict then move it to the left place according to the
    #  matched count index

    matched_count_index = 0

    for digit in range(10):
        if digit_occurrence_count_dict[digit] == 1:
            input_list[matched_count_index] = digit
            matched_count_index += 1

    first_number = 0
    second_number = 0

    # loop through input list indexes inversely from last to start
    # now as we have a sorted input list, we can loop inversely through it
    # and generate two numbers by using odd and even indexes

    last_index_of_input_list = input_list_length - 1

    for index in range(last_index_of_input_list, -1, -1):

        value_at_index = input_list[index]

        # if index is even
        if index % 2 == 0:
            first_number *= 10
            first_number = first_number + value_at_index
            continue

        second_number *= 10
        second_number = second_number + value_at_index

    return [first_number, second_number]
