"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    result = []    
    test = [None] * 1000
    
    for index in range(len(list1)):
        if test[list1[index]] == None:
            result.append(list1[index])
            test[list1[index]] = list1[index]
                          
    return result

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    result = []
    test2 = [None] * 1000
    
    list2 = remove_duplicates(list2)
    
    for idx in range(len(list1)):
        test2[list1[idx]] = list1[idx]
    
    for idx in range(len(list2)):
        if test2[list2[idx]] == list2[idx]:
            result.append(list2[idx])

    return result

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.
 
    This function can be iterative.
    """ 
    result = []
    check = True
    idx = 0
    while list1 != [] and list2 != [] and check:
        if list1[idx] < list2[idx]:
            result.append(list1[idx])
            list1 = list1[idx + 1 :]
        else:
            result.append(list2[idx])
            list2 = list2[idx + 1 :]
        check = idx <= len(list1)
            
    # there might be some elements remaining in left 
    # or right subarrays
    check = True
    while list1 != [] and check:
        result.append(list1[idx])
        list1 = list1[idx + 1 :]
        check = idx <= len(list1)
        
    check = True       
    while list2 != [] and check:
        result.append(list2[idx])
        list2 = list2[idx + 1 :]
        check = idx <= len(list2)
            
    return result
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    # base case: a list of non-zero elements are sorted by definition
    if len(list1) <= 1:
        return list1
    
    # split the arrays by the middle and assign the halfs to
    # left and right respectively
    middle = len(list1) // 2
    left, right = list1[:middle], list1[middle:]
    
    # recursively sort both the halves
    left = merge_sort(left)
    right = merge_sort(right)
    
    # merge the now sorted sub-arrays
    return merge(left, right)

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    # base case
    if len(word) == 0:
        return [""] 
    
    # split the input string into two parts
    # the first character and the remaining characters (rest)
    first = word[0]
    rest = word[1:]
    
    # use gen_all_strings to generate all the possible strings for rest
    rest_strings = gen_all_strings(rest)
    new_strings = []
    for item in rest_strings:
        for idx in range(len(item) + 1):
            new_strings.append(item[:idx] + first + item[idx:])
    
    return  new_strings + gen_all_strings(rest)

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    return []

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()

    
    
