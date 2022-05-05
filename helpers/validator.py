"""
Utils functions for validate
the keys of the json requests.
"""

def are_valid_keys(json_clothe:dict) -> bool:
  """
  Validate if the keys of the json clothe passed
  are valid.

  Return True is are valid
  """

  if 'name' in json_clothe and 'price' in json_clothe and 'size' in json_clothe:
    return True
  else:
    return False