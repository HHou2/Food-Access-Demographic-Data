"""
HHou2
March 2023
SSQL Project: Food Access Demographic Data
backend
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

def runSearch(data_as_txt, search_type, target_search, from_idxs):
  """
  Runs the search, depending on the user's choice

  Parameters:
    data_as_txt: (lst) list of all lines from file as text
    search_type: (int) the type of search
    the user has chosen
    target: (str) the search field intended by the user
    from_idxs: (lst) list of indexes to search from

  Returns:
    target_idxs: (lst) a list of indexes (int) for when target hit within lines
    or if the user wants to quit, returns "end" (str)

    i. If user chooses 1: linear search by state.
    ii. If user chooses 2: linear search by population threshold
  """

  if search_type == 1:
    print()
    target_idxs = state_search(data_as_txt, target_search, from_idxs)
    return target_idxs

  elif search_type == 2:
    print()
    target_idxs = pop_search(data_as_txt, target_search, from_idxs)
    return target_idxs

def state_search(data_as_txt, target, from_idxs):
  """
  Runs a linear search for state names.

  Parameters:
    data_as_txt: (lst) list of lines to search
    target: (str) string targetting in the search
    from_idxs: (lst) list of indexes to search from
  Returns:
    target_idxs: (lst) list of indexes when target is present in lst
  """

  target_idxs = []

  for i in range(len(from_idxs)):
    if target.lower() in data_as_txt[(from_idxs[i])][0:len(target)].lower():
      target_idxs.append(from_idxs[i])
  return target_idxs

def pop_search(data_as_txt, target, from_idxs):
  """
  Performs a linear search for indexes with a population within the target 
  range.

  Parameters:
    data_as_txt: (lst) list of lines to search
    target: (lst) list of targetted population range target[0] is the minimum
    and target[1] is the maximum.
    from_idxs: (lst) list of indexes to search from
  Returns:
    target_idxs: (lst) list of indexes when target is present in lst
  """

  target_idxs = []

  for i in range(len(from_idxs)):
    if (int(target[0]) < int(data_as_txt[from_idxs[i]])) and (int(target[1]) > int(data_as_txt[from_idxs[i]])):
      target_idxs.append(from_idxs[i])
  
  return target_idxs

def runSort(sort_type, data_as_obj, from_idxs):
  """
  Runs the search, depending on the user's choice

  Parameters:
    sort_type: (int) the type of sort the user has chosen
    data_as_obj: (int) the data as objects
    from_idxs: (lst) indexes from which to sort
  Returns:
    ordered_idxs: (lst) a list of indexes (int) for the re-ordered list

    i. If user chooses 3: selection sort for state
    ii. If user chooses 4: insertion sort by population
  """

  state_as_txt_sort = []
  for row in range(len(from_idxs)):
    state_as_txt_sort.append(data_as_obj[from_idxs[row]].get_state())

  pop_as_txt_sort = []
  for row in range(len(from_idxs)):
    pop_as_txt_sort.append(data_as_obj[from_idxs[row]].get_population())

  if sort_type == 3:
    print()
    ordered_idxs = state_sort(from_idxs, state_as_txt_sort)
    return ordered_idxs

  elif sort_type == 4:
    print()
    ordered_idxs = pop_sort(from_idxs, pop_as_txt_sort)
    return ordered_idxs

def state_sort(from_idxs, data_as_txt):
  """
  Performs a selection sort for the indexes for state names.

  Parameters:
    from_idxs: (lst) list of indexes from which to sort
    data_as_txt: (lst) list of all lines from file as text
  Returns:
    ordered_idxs: (lst) a list of indexes (int) of the order 
  """

  list_to_order = data_as_txt
  idxs_to_order = from_idxs

  for i in range(len(idxs_to_order)):
    smallest = find_smallest(list_to_order, i)
    swap(list_to_order, i, smallest)
    swap(idxs_to_order, i, smallest)

  return idxs_to_order

def pop_sort(from_idxs, data_as_txt):
  """
  Performs an insertion sort for the indexes by population size (increasing
  order).

  Parameters:
    from_idxs: (lst) list of target indexes to order
    data_as_txt: (lst) list of all lines from file as text
  Returns:
    idxs_to_order: (lst) list of indexes ordered by corresponding population
  """

  lst_to_order = data_as_txt
  idxs_to_order = from_idxs

  for i in range(len(idxs_to_order)):
      smaller_idx = i

      while ((smaller_idx) > 0) and int(data_as_txt[smaller_idx]) < int(lst_to_order[smaller_idx - 1]):
        swap(lst_to_order, smaller_idx, smaller_idx - 1)
        swap(idxs_to_order, smaller_idx, smaller_idx - 1)
        smaller_idx = smaller_idx - 1

  return idxs_to_order