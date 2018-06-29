from jsonschema import validate

schema = {
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
        "username": {"type": "string"},
        "contact": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{6}"}
    },
    "required": ["username", "contact"]
}
