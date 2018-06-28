from jsonschema import validate

schema = {
    "type":"object",
    "properties": {
        "route":{"type": "string"},
        "driver": {"type": "string"},
        "fare": {"type": "integer"}
    },
    "required":["route", "driver", "fare"]
}
