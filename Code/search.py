#!python


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # pass
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests
    if index >= len(array):
        # item not found
        return None

    if item == array[index]:
        # item found
        return index
    else:
        index += 1
        # keep searching and call function again
        return linear_search_recursive(array, item, index)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_recursive(array, item)
    return binary_search_iterative(array, item, left=0, right=len(array) - 1)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # pass
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    left = 0
    right = len(array) - 1

    while left <= right:
        if array[mid] == item:
            return mid
        elif array[mid] > item:
            right = mid - 1

        elif array[mid] < item:
            left = mid + 1
        return None


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    # pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
    if left > right:
        return None

    mid = round((left + right)/2)

    if array[mid] == item:
        return mid

    elif array[mid] == item:
        right = mid - 1
        return binary_search_recursive(array, item, left, right)

    elif array[mid] < item:
        left = mid + 1
        return binary_search_recursive(array, item, left, right)
