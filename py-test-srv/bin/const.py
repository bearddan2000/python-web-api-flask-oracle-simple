URL = 'http://py-srv:5000'

GET_ALL_URL = URL + '/dog'

GET_BY_FILTER_URL = URL + '/dog/breed/Labrador'

STATIC = {  
    "results": [
    {
      "breed": "Am Bulldog",
      "color": "White",
      "id": 1
    },
    {
      "breed": "Blue Tick",
      "color": "Grey",
      "id": 2
    },
    {
      "breed": "Labrador",
      "color": "Black",
      "id": 3
    },
    {
      "breed": "Gr Shepard",
      "color": "Brown",
      "id": 4
    }
  ]
}

DELETE_URL = URL + '/dog/id/1'

INSERT_URL = URL + '/dog/breed/Poodle/color/Pink'

SMOKE_URL = URL + '/'

SMOKE = {"results": {"hello": "world"}}

UPDATE_URL = URL + '/dog/id/2'
