# Clothes Restapi

A Restapi made with python using sqlite3 database.

## Manual Installation

```bash
$ git clone https://github.com/EduardYan/clothes-restapi.git
$ cd clothes-restapi
$ pip3 install -r ./requirements.txt
```

## Running

Only execute the file index.py

```bash
$ python3 index.py
```

## Routes

### GET
* Get a list of clothes in the database  __/clothes__
* Get a clothe for your id in the database  __/clothe/1__

### POST
* Send a new clothe for save in the database __/add-clothe/__

### PUT
* Update a clothe, indicating your id and the new values __/update-clothe/1__

In case of POST and PUT request the new data to send must be this json object
```json
{
  "name": "Pants",
  "price": 15,
  "size": "M"
}
```

### DELETE
* Delete a clothe in the database using your id __/delete-clothe/1__

In each request you will receive a message with extra information to use.