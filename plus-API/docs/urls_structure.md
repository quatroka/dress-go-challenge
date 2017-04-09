# Urls Structure

## Places

### Places - Create
Create a place on system.

> *POST*

    /api/places
    
Example usage:

    curl -H "Content-Type: application/json" -X POST -d '{ "place": "Dress & Go" }' http://localhost:5000/api/places

Success 200

| Field           | Type   | Description              |
| --------------- | ------ | ------------------------ |
| _id             | Int    | Database Place Id.       |
| place_name      | String | Full place adress.       |
| latitude        | Number | Latitude of place.       |
| longitude       | Number | Longitude of place.      |
| google_place_id | String | Google place id of place |

---

### Places - Delete
Delete a place on system.

> *DELETE*

    /api/places/:id

Example usage:

    curl -H "Content-Type: application/json" -X DELETE http://localhost:5000/api/places/[id]

Parameter

| Field | Type    | Description |
| ----- | ------- | ----------- |
| id    | Integer | Place's ID. |

204

| Field | Description |
| ----- | ----------- |
| body  | No Content. |

---

### Places - Get One
Fetches a place data on system.

> *GET*

    /api/places/:id

Example usage:

    curl -H "Content-Type: application/json" -X DELETE http://localhost:5000/api/places/[id]

Parameter

| Field | Type    | Description |
| ----- | ------- | ----------- |
| id    | Integer | Place's ID. |

---

### Places - List
Fetches a list of places data on system.

> *GET*

    /api/places/:id

Example usage:

    curl -H "Content-Type: application/json" -X DELETE http://localhost:5000/api/places/

Success 200

| Field  | Type     | Description       |
| ------ | -------- | ----------------- |
| places | Object[] | A list of places. |
