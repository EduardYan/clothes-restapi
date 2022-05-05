#!/usr/bin/env python3

"""
Principal file for execute the
RESTAPI.
"""

from app import restapi
from helpers.config import CONFIG, ConfigObjectInvalid
from helpers.db import db

if __name__ == '__main__':

  # creating tables
  with restapi.app_context():
    db.create_all()

  try:
    restapi.run(
      port = CONFIG['PORT'],
      host = CONFIG['HOST'],
      debug = CONFIG['DEBUG'],
    )

  except ConfigObjectInvalid as e:
    print(e)