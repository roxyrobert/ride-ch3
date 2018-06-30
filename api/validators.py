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
        "passenger": {"type": "string"},
        "ride": {"type": "string"}
    },
    "required": ["passenger", "ride"]
}
