# STEP 1
def split(array):
    """
    Splits a list into two pieces
    :param input_list: list
    :return: left and right lists (list, list)
    """
    array_len = len(array)
    center = array_len // 2
    return array[:center], array[center:]


# STEP 2
def merge_sorted_lists(left_list, right_list):
    # Special case: one or two lists are empty
    if len(left_list) == 0:
        return right_list
    elif len(right_list) == 0:
        return left_list

    index_left = index_right = 0
    merge_list = []
    merge_list_len = len(left_list) + len(right_list)

    while len(merge_list) < merge_list_len:
        # value of the left list is less
        if left_list[index_left] <= right_list[index_right]:
            merge_list.append(left_list[index_left])
            index_left += 1
        else:
            # value of the right list is less
            merge_list.append(right_list[index_right])
            index_right += 1
        # Check for the end of the list
        # right end reached
        if index_right == len(right_list):
            merge_list += left_list[index_left:]
            break
        # left end reached
        if index_left == len(left_list):
            merge_list += right_list[index_right:]
            break
    return merge_list


# STEP 3
def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        left, right = split(array)
        # the most important line
        return merge_sorted_lists(merge_sort(left), merge_sort(right))


print(merge_sort([3, 6, 9, 1, 8, 4, 13, 45, 11, 2, 78, 47, 99, 86, 45]))
