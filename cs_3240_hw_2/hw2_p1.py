def maxmin(list):
    """
    scans the list and finds the minimum and maximum values, returning them in a tuple of the form (max, min)
    :param list:
    :return ret_max, ret_min: a tuple containing the maximum value and minimum value found in the list
    """
    length = len(list)

    ret_min = list[0]
    ret_max = list[0]

    for i in range(1, length):
        if list[i] < ret_min:
            ret_min = list[i]
        if list[i] > ret_max:
            ret_max = list[i]

    return ret_max, ret_min


def common_items(list1, list2):
    """
    returns a list of the items that exist in both lists
    :param list1:
    :param list2:
    :return ret_list:
    """
    ret_list = []

    for item in list1:
        if (item in list2) and (item not in ret_list): # add no duplicates
            ret_list.append(item)

    return ret_list


def notcommon_items(list1, list2):
    """
    returns a list of the items that exist in one list or the other but not both;
    i.e., notcommon([0,1,2,3],[2,3,4,5]) -> [0,1,4,5]
    :param list1:
    :param list2:
    :return:
    """
    unique_items = []

    for item in list1:
        if item not in list2:
            unique_items.append(item)

    for item in list2:
        if item not in list1:
            unique_items.append(item)

    return unique_items


def count_list_items(list):
    """
    returns a dictionary containing the frequency count of each item in the list
    :param list:
    :return counts: a dictionary with the list items as keys and integer values
    """
    counts = {}

    list_set = common_items(list,list)

    for set_item in list_set:
        counts[set_item] = 0
        for list_item in list:
            if set_item == list_item:
                counts[set_item] += 1

    return counts





