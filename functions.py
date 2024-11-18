# TODO: Implement the following functions based on the descriptions.

def reverse_list(lst):
    reversed_list = []
    rev_string = str(lst[::-1])
    reversed_list.append(rev_string)
    print(reversed_list)
    
reverse_list([1, 2, 3, 4, 5, 6])
# """
#     Reverses the given list.
#     :param lst: List of integers.
#     :return: A list with elements in reverse order.
#     """
#     pass  # Implement this

def count_occurrences(lst, element):
    every_element = 0
    for i in lst:
        if i == element:
            every_element += 1
    print(every_element)
count_occurrences([1, 2, 3, 4, 4, 5, 6, 1, 3, 4, 2, 5 ,5, 6], 6)
# """
#     Counts how many times the given element appears in the list.
#     :param lst: List of elements.
#     :param element: Element to count.
#     :return: Integer count of occurrences.
#     """
#     pass  # Implement this

def get_keys_with_value(dct, value):
    list_of_keys = []
    for keys in dct:
        if value == dct.values():
            list_of_keys.append(dct.keys)
    print(list_of_keys)
    
    # dct = {
    #     'almonds': 24,
    #     'brazil nuts': 13,
    #     'cashews' : 6,
    #     'hazelnuts' : 19
    # }
get_keys_with_value(dct = {
        'almonds': 24,
        'brazil nuts': 13,
        'cashews' : 6,
        'hazelnuts' : 19
    }, value = 19)
        
"""
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
#     pass  # Implement this

def merge_sorted_lists(lst1, lst2):
    # KYLE: you never said we should sort the list again...
    sort_lst1 = lst1.sort()
    sort_lst2 = lst2.sort()
    merged_list = []
    
    for i in lst1:
        merged_list.append(i)
    for j in lst2:
        merged_list.append(j)
        
    print(merged_list)
merge_sorted_lists([3, 7, 9, 17, 12, 91, 6], [9, 8, 7, 6, 5, 4])
"""
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
#     """
#     pass  # Implement this

def find_second_largest(numbers):
    for i in numbers:
        numbers.sort()
    second_largest = numbers[:-2]
    
print(second_largest)
find_second_largest([8, 7, 12, 71, 19, 3, 14, 57, 6, 21])
"""
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """
#     pass  # Implement this

def is_anagram(str1, str2):

    anagram_count = 0
    first_str_length = len(str1)
    second_str_length = len(str2)
    if first_str_length == second_str_length:
        for char in str1:
            for letter in str2:
                if char == letter:
                    anagram_count+= 1
            if anagram_count == first_str_length:
                is_an_anagram = True
            else:
                is_an_anagram = False
    print(is_an_anagram)
is_anagram('pear', 'reap')
        
"""
    Checks if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.
    
    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
#     pass  # Implement this


# def flatten_list(nested_list):
#     """
#     Flattens a nested list into a single list.
#     :param nested_list: List of lists.
#     :return: A flat list with all elements.
#     """
#     pass  # Implement this


def remove_duplicates(lst):
    no_dupes = []
    for i in lst:
        if i not in no_dupes:
            no_dupes.append(i)
    print(no_dupes)
remove_duplicates([1, 2, 2, 2, 3, 4, 4, 5, 6, 7, 8])
"""
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
#     pass  # Implement this

def find_common_elements(lst1, lst2):
    common_elements = []
    for i in lst1:
        for j in lst2:
            if i == j:
                common_elements.append(i)
    print(common_elements)
find_common_elements(['ari', 'bey', 'carly', 'donna', 'emma'],['ari','bella', 'carly', 'dean', 'emma'])

"""
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
#     """
#     pass  # Implement this