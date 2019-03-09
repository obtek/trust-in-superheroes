import pytest

def test_get_index(client):
    rv = client.get('/heroes')
    assert rv.status_code == 200

'''
*Psuedo Tests*

Test the app routes: 
- assert all routes return the expected status codes (i.e., 200, 201, 409, 404)
- assert that a POST request with proper data creates a new superhero
- assert that a POST request with duplicate data does not create a new superhero
- assert that query params effectively filter the data

Test the models  (ideally, placed in a different file):
- assert that the proper facilitates the creation of new models
- assert that incomplete or conflicting data cannot create a new model, e.g., a superhero_alias already in the db
'''

