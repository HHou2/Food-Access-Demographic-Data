"""
HHou2
March 2023
SSQL Project: Food Access Demographic Data
main.py
"""

from frontend import *
from backend import *
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

main()