"""
HHou2
March 2023
SSQL Project: Food Access Demographic Data
displays
"""

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