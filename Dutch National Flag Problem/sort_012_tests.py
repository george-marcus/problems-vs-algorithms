from sort_012 import sort_012


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)

    if not test_case and sorted_array is None:
        print("Pass")

    elif sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
               2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0, 1, 2])
test_function([0, 1])
test_function([0])
test_function([])
test_function(None)
