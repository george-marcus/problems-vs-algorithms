from rearrange_digits import rearrange_digits


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[4, 6, 2, 5, 8], [864, 52]])
test_function([[0, 1], [1, 0]])
test_function([[0, 1, 1], [11, 0]])
