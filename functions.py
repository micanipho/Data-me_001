

def reverse_list(lst):
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    param_lst = lst[::-1]
    return param_lst


def count_occurrences(lst, element):
    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    count = 0
    for num in lst:
        if num == element:
            count += 1
    return count


def get_keys_with_value(dct, value):
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    _list = []
    for word in dct.keys():
        if value == dct[word]:
            _list.append(word)
    #print(_list)              
    return _list
        

    
#get_keys_with_value({'a': 1, 'b': 2, 'c': 1}, 1)

def merge_sorted_lists(lst1, lst2):
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
    
    merge_sorted_lists = sorted((lst1 + lst2))
    return merge_sorted_lists
    
#print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))

def find_second_largest(numbers):
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """
    if len(numbers) == 1:
        return None
    else:
        param_numbers = sorted(numbers)
        if numbers[-1] == numbers[-2]:
            return None
        else:
            return numbers[-2]  
#print(find_second_largest([1, 2, 3, 4]))

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
        for character in str1:
                if character in str2:
                    return True
                else:
                    return False
    
#print(is_anagram("listen", "silent"))


def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
    _lst = []
    for i in nested_list:
        _lst.extend(i)
    return _lst
        

print(flatten_list([[1], [], [2, 3]]))
def remove_duplicates(lst):
    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    _list = []
    for i in range(len(lst)-1):
        if not lst[i] in _list:
            _list.append(lst[i])
    return _list
    
    
#print(remove_duplicates([1, 2, 2, 3, 3]))  

def find_common_elements(lst1, lst2):
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    _lst = []
    for num  in lst1:
        if num in lst2:
            _lst.append(num)
    return _lst
    

#print(find_common_elements([1, 2, 3], [3, 4, 5]))