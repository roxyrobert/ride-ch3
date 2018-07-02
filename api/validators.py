from jsonschema import validate

users_schema = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "password": {"type": "string"},
        "contact": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{6}"}
    },
    "required": ["username", "email", "password", "contact"]
}

create_ride_schema = {
    "type": "object",
    "properties": {
        "route": {"type": "string"},
        "driver": {"type": "string"},
        "fare": {"type": "integer"}
    },
    "required": ["route", "driver", "fare"]
}

join_ride_schema = {
    "type": "object",
    "properties": {
        "passenger": {"type": "string"},
        "ride": {"type": "string"}
    },
    "required": ["passenger", "ride"]
}
