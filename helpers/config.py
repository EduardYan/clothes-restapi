"""
Utils functions to use
for the configuration.
"""

from json import load


class ConfigObjectInvalid(TypeError):
  """
  Model for the exception in case
  not is valid the config object.
  """

  pass

def get_config_object() -> dict:
  """
  Return a dictionary with
  the content of the file './conf.json'
  """

  with open('./conf.json', 'r') as f:
    OBJECT = load(f)
    f.close()

  return OBJECT

def validate_config_object(object:dict):
  """
  Validate the config object passed
  for parameter.

  Except is lauch if the config object
  not is valid.
  """

  # allow keys to validate
  ALLOW_KEYS = ['PORT', 'HOST', 'DEBUG', 'SQLITE_DB_PATH']

  for key in ALLOW_KEYS:
    if key not in object:
      raise ConfigObjectInvalid('The config object not is valid. Verify the keys and values.')


# config file to use
CONFIG = get_config_object()
validate_config_object(CONFIG)