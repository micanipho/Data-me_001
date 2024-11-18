# TODO: Implement the following functions based on the descriptions.

def reverse_list(lst):
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    new_list=lst[::-1]
    return new_list


def count_occurrences(lst, element):
    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    count=0
    for i in lst:

        if i==element:
            count +=1
    return count


def get_keys_with_value(dct, value):
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    key_list=[]
    for key, i in dict.items(dct):
        if i==value:
            key_list.append(key)
    return key_list


def merge_sorted_lists(lst1, lst2):
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
    new_list=lst1.extend(lst2)
    return new_list.sort()

def find_second_largest(numbers):
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    1,4,6,7
    """
    highest_number=0
    highest=[]
    for i in numbers:
        if i > highest_number:
            highest_number=i
            highest.append(highest_number)
    second_largest=highest[-2]
    return second_largest

        

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
    else:
        for x in str1:
            if x in str2:
                pass
        

def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
    nested_list=[]



def remove_duplicates(lst):
    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    duplicates_list=[]
    for x in lst:
        if x not in duplicates_list:
            duplicates_list.append(x)
        else :pass
    return duplicates_list



def find_common_elements(lst1, lst2):
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    common_list=[]
    for x in lst1:
        for y in lst2:
            if y==x:
                common_list.append(x)
    return common_list
