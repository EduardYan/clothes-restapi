"""
This file have the routes
to use in the restapi.
"""

from flask import (
  Blueprint,
  render_template,
  request,
  jsonify,
)
from models.clothe import Clothe
from helpers.db import db
from helpers.validator import are_valid_keys

# routes
restapi_routes = Blueprint('restapi', __name__)

@restapi_routes.route('/')
def index():
  """
  Principal route for the restapi,
  return the list clothes in the database.
  """

  return render_template('index.html')

@restapi_routes.route('/clothes')
def clothes_handler():
  """
  Return a list of clothes json objects.
  """

  # getting all clothes
  clothes = Clothe.query.all()
  clothes_objects = []

  for clothe in clothes:
    object = {
      'name': clothe.name,
      'price': clothe.price,
      'size': clothe.size,
    }
    clothes_objects.append(object)

  return jsonify({
    'clothes': clothes_objects,
  })


@restapi_routes.route('/clothe/<int:id>')
def clothe_handler(id):
  """
  Return a clothe json object
  """

  # clothe found for id
  clothe_found = Clothe.query.filter_by(id = int(id)).first()
  if clothe_found == None:
    return jsonify({
      'message': 'The clothe id not found.',
    })

  else:
    object = {
      'name': clothe_found.name,
      'price': clothe_found.price,
      'size': clothe_found.size,
    }

    return jsonify({
      'clothe': object,
    })

@restapi_routes.route('/add-clothe', methods = ['POST'])
def add_clothe():
  """
  Add the clothe recived in the json
  request in the database.
  """

  if request.method == 'POST':
    # only if is json request
    if request.is_json:
      # getting
      json_clothe = request.get_json()

      # validating the keys
      if are_valid_keys(json_clothe):
        clothe = Clothe(
          json_clothe['name'],
          json_clothe['price'],
          json_clothe['size']
          )

        try:
          db.session.add(clothe)
          db.session.commit()
        except:
          return jsonify({'message': 'Some error to save in the database.'})

        new_clothes = Clothe.query.all()
        new_clothes_objects = []

        for clothe in new_clothes:
          object = {
            'name': clothe.name,
            'price': clothe.price,
            'size': clothe.size,
          }

          new_clothes_objects.append(object)

        return jsonify({
          'message': 'Clothe added succesfully.',
          'newClothes': new_clothes_objects,
        })

      else:
        return jsonify({
          'message': 'Verify the keys allowed for send a new clothe. Clothe not saved.'
        })

    else:
      return jsonify({
        'message': 'The request not is a json object.'
      })


@restapi_routes.route('/update-clothe/<int:id>', methods = ['PUT'])
def update_clothe(id):
  """
  Update the clothe for the id passed in url,
  with the new data to set.
  """

  if request.method == 'PUT':
    if request.is_json:
      # new data to set
      json_clothe = request.get_json()

      if are_valid_keys(json_clothe):
        # getting the clothe to update
        clothe = Clothe.query.filter_by(id = int(id)).first()

        # old data
        old_clothe = {
          'name': clothe.name,
          'price': clothe.price,
          'size': clothe.size,
        }

        clothe.name = json_clothe['name']
        clothe.price = int(json_clothe['price'])
        clothe.size = json_clothe['size']

        # new data
        new_clothe = {
          'name': clothe.name,
          'price': clothe.price,
          'size': clothe.size,
        }
        
        try:
          db.session.add(clothe)
          db.session.commit()

          return jsonify({
            'message': f'Clothe with id {clothe.id} updated.',
            'oldClothe': old_clothe,
            'newClothe': new_clothe,
            })

        except:
          return jsonify({'message': 'Some error to update in the database.'})

      else:
        return jsonify({
          'message': 'Verify the keys allowed for send a new clothe. Clothe not update.',
        })
    
    else:
      return jsonify({
        'message': 'The request not is a json object.',
      })

@restapi_routes.route('/delete-clothe/<int:id>', methods = ['DELETE'])
def delete_clothe(id):
  """
  Delete the clothe for the id passed in url.
  """

  if request.method == 'DELETE':
    # getting to delete
    clothe = Clothe.query.filter_by(id = int(id)).first()

    deleted_clothe = {
      'name': clothe.name,
      'price': clothe.price,
      'size': clothe.size,
    }

    try:
      db.session.delete(clothe)
      db.session.commit()

      return jsonify({
        'message': f'Clothe with id {clothe.id} deleted.',
        'deletedClothe': deleted_clothe,
      })

    except:
      return jsonify({'message': 'Some error to delete in the database.'})