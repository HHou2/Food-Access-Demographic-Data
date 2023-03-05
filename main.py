"""
HHou2
March 2023
SSQL Project: Food Access Demographic Data
main.py
"""

from algorithms import *
from frontend import *
from record import Record

def main():
    """
    The main function.

    Parameters:
      None
    Returns:
      None

    1. Run the search
    2. End program message
    """

    file = open("Food Access Demographic Data/food_access.csv")
    raw_data = (file.readlines())
    file.close()

    data_as_txt = [] # list of every record by text format
    data_as_obj = [] # list of every record by object format

    for i in range(len(raw_data) - 1):
        data_as_txt.append(raw_data[i + 1]) # note i + 1 to exclude record 1

        tmp_record = raw_data[i + 1] # note i + 1 to exclude record 1
        split_record = tmp_record.split(",")

        data_as_obj.append(Record(split_record[0], split_record[1], \
            split_record[2], split_record[3], split_record[4], \
                split_record[5], split_record[6].strip("\n")))

    program_continue = True
    while program_continue == True:
        program_continue = runProgram(data_as_obj)

    endProgram()

def runProgram(data_as_obj):
  """
  Runs a search of a user-specified criteria and then displays the
  information formatted.

  Parameters:
    data_as_obj: (lst) list of records as objects
  Returns:
    none

  a. Prompt user for results
  b. Run the search, based on user input.
  c. Display formatted result
  d. Go back to prompt user for results (looping)
  """

  state_as_txt = []
  for row in range(len(data_as_obj)):
    state_as_txt.append(data_as_obj[row].get_state())

  pop_as_txt = []
  for row in range(len(data_as_obj)):
    pop_as_txt.append(data_as_obj[row].get_population())

  from_idxs = []
  for i in range(len(data_as_obj)):
    from_idxs.append(i)

  original_from_idxs = from_idxs

  choice = getValidChoice()

  while choice[0] != 0:
    if choice[0] == 1:
      data_as_txt_to_use = state_as_txt
    elif choice[0] == 2:
      data_as_txt_to_use = pop_as_txt
    elif choice[0] == 3:
      pass
    elif choice[0] == 4:
      pass
    elif choice[0] == 5:
      from_idxs = original_from_idxs
      print()
      print("Resetting list to contain all records... ")

    if (choice[0] == 1) or (choice[0] == 2):    # searching
      target_idxs = runSearch(data_as_txt_to_use, choice[0], choice[1], from_idxs)
      from_idxs = target_idxs
      if target_idxs != []:
        displayResult(data_as_obj, target_idxs)
      elif target_idxs == []:
        print("No records found!")
    elif (choice[0] == 3) or (choice[0] == 4):  # sorting
      ordered_idxs = runSort(choice[0], data_as_obj, from_idxs)
      from_idxs = ordered_idxs
      if ordered_idxs != []:
        displayResult(data_as_obj, ordered_idxs)
      elif target_idxs == [1]:
        print("No items to sort!")

    print()
    choice = getValidChoice()

  return False

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

main()