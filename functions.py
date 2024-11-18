# TODO: Implement the following functions based on the descriptions.

def reverse_list(lst):
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    return lst[::-1]

def count_occurrences(lst, element):
    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    freq = [e for e in lst if e == element]

    return len(freq)

def get_keys_with_value(dct, value):
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    lst_keys = [k for k,v in dct.items() if v == value]

    return lst_keys

def merge_sorted_lists(lst1, lst2):
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
    std_lst = lst1 + lst2

    return sorted(std_lst)

def find_second_largest(numbers):
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """
    nums = set(sorted(numbers))

    if len(nums) < 2:
        return None
    
    return list(nums)[-2]


def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.
    
    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
    if len(str1) != len(str2):
        return False
    
    for c in str1:
        if c in str2:
            continue
        else:
            return False
    
    return True


def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
    flattened_lst = []

    for i in nested_list:
        if isinstance(i, list):
            flattened_lst += i
        else:
            flattened_lst.append(i)

    return flattened_lst


def remove_duplicates(lst):
    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    unduplicated_lst  = []

    for c in lst:
        if unduplicated_lst.count(c) == 0:
            unduplicated_lst.append(c)

    return unduplicated_lst

def find_common_elements(lst1, lst2):
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    common_lst = [c for c in lst1 if c in lst2]

    return common_lst
