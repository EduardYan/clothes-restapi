"""
Model for a clothe
in the database.
"""

from helpers.db import db

class Clothe(db.Model):
  """
  Model for a clothe for the database.
  """

  # columns
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(80))
  price = db.Column(db.Integer)
  size = db.Column(db.Integer)

  def __init__(self, name:str, price:float, size:str) -> None:
    # values
    self.name = name
    self.price = price
    self.size = size