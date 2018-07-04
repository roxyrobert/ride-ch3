from jsonschema import validate

users_schema = {
    "type": "object",
    "properties": {
        "username": {"type": "string", "maxLength": 10,
            "minLength": 3},
        "email": {"type": "string", "maxLength": 30,
            "minLength": 5},
        "password": {"type": "string", "maxLength": 30,
            "minLength": 8},
        "contact": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{6}"}
    },
    "required": ["username", "email", "password", "contact"]
}

login_schema = {
    "type": "object",
    "properties": {
        "email": {"type": "string", "maxLength": 30,
            "minLength": 6},
        "password": {"type": "string", "maxLength": 30,
            "minLength": 3}
    },
    "required": ["email", "password"]
}

create_ride_schema = {
    "type": "object",
    "properties": {
        "route": {"type": "string", "maxLength": 10,
            "minLength": 3},
        "driver": {"type": "string", "maxLength": 10,
            "minLength": 1},
        "fare": {"type": "integer"}
    },
    "required": ["route", "driver", "fare"]
}

join_ride_schema = {
    "type": "object",
    "properties": {
        "passenger": {"type": "string", "maxLength": 10,
            "minLength": 1},
        "ride": {"type": "string", "maxLength": 10,
            "minLength": 1}
    },
    "required": ["passenger", "ride"]
}
