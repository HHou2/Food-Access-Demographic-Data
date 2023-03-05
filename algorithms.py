"""
HHou2
March 2023
SSQL Project: Food Access Demographic Data
algorithms
"""

def swap(lst, i, j):
    """
    Swaps the items in a function based on index.

    Parameters:
        lst: (lst) list of items
        i: (int) index of first item to swap
        j: (int) index of second item to swap
    Returns:
        none
    """

    tmp  = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp

def selection_sort(lst):
    """
    Uses a selection sorting algorithm to sort a list.

    Parameters:
        lst: (lst) list to sort
    Returns:
        sorted_lst: (lst) sorted list
    """

    for i in range(len(lst)):
        smallest_idx = i
        for j in range(i, len(lst)):
            if lst[j] < lst[smallest_idx]:
                smallest_idx = j
        swap(lst, i, smallest_idx)

    return lst

def lookbefore(lst):
    """
    Looks recursively for the same item as the last index.

    Parameters:
        lst: (lst) ordered list of items to search within
        start: (int) inddx to start (before) search for
    Returns:
        idxs_found: (lst) list of indexes when item in lst
    """

    item = lst[len(lst)-1]
    idxs_found = []

    lst = lst[:len(lst)-1]

    look = True
    while look:
        if lst[:len(lst) - 1] == []:
            look = False
            return idxs_found
        elif lst[len(lst) - 1] == item:
            idxs_found.append(len(lst) - 1)
            lst = lst[:len(lst) - 1]
        elif lst[len(lst[:1]) - 1] != item:
            look = False
            return idxs_found

def lookafter(lst):
    """
    Looks recursively for the same item as the first index.

    Parameters:
        lst: (lst) ordered list of items to search within
        start: (int) index to start (afterwards) search for
    Returns:
        idxs_found: (lst) list of indexes when item in lst
    """

    item = lst[0]
    idxs_found = []

    lst = lst[1:]

    i = 1
    look = True
    while look:
        if lst[1:] == []:
            look = False
            return idxs_found
        elif lst[0] == item:
            idxs_found.append(i)
            lst = lst[1:]
            i += 1
        elif lst[0] != item:
            look = False
            return idxs_found

def binary_search(lst, item):
    """
    Uses a binary searching algorithm to find an item in an ordered list.
    
    Parameters:
        lst: (lst) list to search within
        item: (str) item to search for
    Returns:
        idxs_found: (lst) list of indexes when item in lst
    """

    idxs_found = []

    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if item == lst[mid]:
            idxs_found.append(mid)

            # check indexes immediately before mid
            indexes_before_mid = lookbefore(lst[0:mid + 1])
            for i in range(len(indexes_before_mid)):
                idxs_found.append(indexes_before_mid[i])

            # check indexes immediately after mid
            indexes_after_mid = lookafter(lst[mid:])
            for i in range(len(indexes_after_mid)):
                idxs_found.append(mid + indexes_after_mid[i])

            return selection_sort(idxs_found)
        elif item < lst[mid]:
            high = mid - 1
        else:
            low = mid + 1

# we may not need this find_smallest function, this was part of the original lab file, works with the previous selection sort functions
def find_smallest(list_to_order, start_idx):
  """
  Finds the smallest value in a list, starting from i

  Parameters:
    list_to_order: (lst) list of items to order
    start_idx: (int) index of first element from which to sort
  Returns:
    smallest_value: (int) smallest value in list_to_order
  """

  smallest_idx = start_idx

  for i in range(start_idx, len(list_to_order)):
    if list_to_order[i] < list_to_order[smallest_idx]:
        smallest_idx = i

  return smallest_idx