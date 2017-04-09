# Urls Structure

## Places

### Places - Create
Create a place on system.

> *POST*

    /api/places
    
Example usage:

    curl -H "Content-Type: application/json" -X POST -d '{ "place": "Dress & Go" }' http://localhost:5000/api/places

Success 200

| Field           | Type    | Description              |
| --------------- | ------- | ------------------------ |
| _id             | Integer | Database Place Id.       |
| place_name      | String  | Place's name.            |
| full_address    | String  | Full place adress.       |
| latitude        | Float   | Latitude of place.       |
| longitude       | Float   | Longitude of place.      |
| google_place_id | String  | Google place id of place |

Not Acceptable 406

| Field    | Type   | Description     |
| -------- | ------ | --------------- |
| Response | String | Error menssage. |

---

### Places - Delete
Delete a place on system.

> *DELETE*

    /api/places/:place

Example usage:

    curl -H "Content-Type: application/json" -X DELETE http://localhost:5000/api/places/[place]

Parameter

| Field | Type   | Description   |
| ----- | ------ | ------------- |
| place | String | Place's name. |

No Content 204

| Field    | Type   | Description       |
| -------- | ------ | ----------------- |
| Response | String | Success menssage. |

Not Acceptable 406

| Field    | Type   | Description     |
| -------- | ------ | --------------- |
| Response | String | Error menssage. |
---

### Places - Get One
Fetches a place data on system.

> *GET*

    /api/places/:place

Example usage:

    curl -H "Content-Type: application/json" -X GET http://localhost:5000/api/places/[place]

Parameter

| Field | Type   | Description   |
| ----- | ------ | ------------- |
| place | String | Place's name. |

Success 200

| Field           | Type   | Description              |
| --------------- | ------ | ------------------------ |
| place_name      | String | Place name.              |
| full_address    | String | Full place adress.       |
| latitude        | Float  | Latitude of place.       |
| longitude       | Float  | Longitude of place.      |
| google_place_id | String | Google place id of place |

Not Found 404

| Field    | Type   | Description     |
| -------- | ------ | --------------- |
| Response | String | Error menssage. |

---

### Places - List
Fetches a list of places data on system.

> *GET*

    /api/places

Example usage:

    curl -H "Content-Type: application/json" -X GET http://localhost:5000/api/places

Success 200

| Field | Type     | Description                              |
| ----- | -------- | ---------------------------------------- |
| place | Object[] | A list of places.(See Places - Get One.) |

Not Found 404

| Field    | Type   | Description     |
| -------- | ------ | --------------- |
| Response | String | Error menssage. |
