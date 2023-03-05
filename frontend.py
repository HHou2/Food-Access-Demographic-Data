"""
HHou2
March 2023
SSQL Project: Food Access Demographic Data
frontend
"""

def getValidChoice():
  """
  Gets a valid choice of the user based on input.

  Parameters:
    none
  Returns:
    [search_type (int), target_search (int or str)]: (lst) the valid user 
    inputted value.

    i. Input for user options: county, state, population, or quit.
    ii. Get valid user input option.
      1. Check if the input is 0, 1, 2, 3, 4, or 5.
        a. If input is: set choice as the input. Proceed to “Run the search.”
        b. If input is not those 4: error message. Go back to “Get valid user 
        input option.”
  """

  print("Please selection one of the following choices:")
  print("1. Filter by state")
  print("2. Filter by population")
  print("3. Sort by state")
  print("4. Sort by population")
  print("5. Reset list")
  print("0. Quit")
  print()

  continue_check = True

  while continue_check == True:
    search_type = input("Enter Selection: ")

    if search_type == "0":
      continue_check = False
      return [0, "none"]
    elif search_type == "1":
      target_search = input("State name (or prefix)? ")
      continue_check = False
      return[1, target_search]
    elif search_type == "2":
      continue_check = False
      continue_target_request1 = True
      while continue_target_request1 == True:
        target_search1 = input("Minimum population? ")
        if (target_search1.isdigit() == True) and (int(target_search1) >= 0):
          continue_target_request1 = False
          min_pop = int(target_search1)
        else:
          print("Error: minimum population must be a positive integer; " + \
            "please try again!")
      continue_target_request2 = True
      while continue_target_request2 == True:
        target_search2 = input("Maximum population? ")
        if (target_search2.isdigit() == True) and (int(target_search2) > \
          int(target_search1)):
          continue_target_request2 = False
          max_pop = int(target_search2)
        else:
          print("Error: Maximum population must be a positive integer" + \
            " greater than the minimum population ; " + \
            "please try again!")
      target_search = [min_pop, max_pop]
      return[2, target_search]
    elif search_type == "3":
      continue_check = False
      return[3, "none"]      
    elif search_type == "4":
      continue_check = False
      return[4, "none"]  
    elif search_type == "5":
      continue_check = False
      return[5, "none"]
    else:
      print("Error! Please enter 0, 1, 2, 3, 4, or 5.")

def shorten_string(string_to_shorten, max_string_length):
  """
  Shortens the string for formatting purposes to 10 characters.

  Parameters:
    string_to_shorten: (str) string to shorten
    max_string_length: (int) maximum length of string
  Returns:
    shortened_string: (str) string that has been shortened

  Shorten string to 10 characters
  """

  shortened_string = string_to_shorten[0:max_string_length]

  return shortened_string

def displayResult(data_as_obj, target_idxs):
  """
  Displays formatted result.

  Parameters:
    data_as_obj: (lst) list of records as texts
    target_idxs: (lst) indexes of the results to display
  Returns:
    none
  """

  print("===============================================================" + 
    "=================")
  print("| %15s | %12s |%9s| %7s| %6s | %6s | %7s|" % ( "County", "State", \
        "Total Pop", "LFA Pop", "Income", "Senior", "Vehicle" ) )
  print("---------------------------------------------------------------" 
    + "-----------------")

  for i in range(len(target_idxs)):
    print("| %15s | %12s |%9s| %7s| %6s | %6s | %7s|" % \
      (shorten_string(data_as_obj[target_idxs[i]].get_county(), 15), \
        (shorten_string(data_as_obj[target_idxs[i]].get_state(), 12)), \
          data_as_obj[target_idxs[i]].get_population(),\
             data_as_obj[target_idxs[i]].get_lfa_pop(), \
              data_as_obj[target_idxs[i]].get_income(), \
                data_as_obj[target_idxs[i]].get_senior(), \
                  data_as_obj[target_idxs[i]].get_vehicle_access()))
  
  print("---------------------------------------------------------------" 
    + "-----------------")
  
def endProgram():
  """
  Ends the program by displaying a goodbye message.
  """
  
  print("Goodbye!")