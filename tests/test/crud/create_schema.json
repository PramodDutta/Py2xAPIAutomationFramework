{
    "$schema": "https://json-schema.org/draft/2019-09/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "required": [
        "bookingid",
        "booking"
    ],
    "additionalProperties": true,
    "properties": {
        "bookingid": {
            "type": "integer"
        },
        "booking": {
            "type": "object",
            "required": [
                "firstname",
                "lastname",
                "totalprice",
                "depositpaid",
                "bookingdates",
                "additionalneeds"
            ],
            "additionalProperties": true,
            "properties": {
                "firstname": {
                    "type": "string"
                },
                "lastname": {
                    "type": "string"
                },
                "totalprice": {
                    "type": "integer"
                },
                "depositpaid": {
                    "type": "boolean"
                },
                "bookingdates": {
                    "type": "object",
                    "required": [
                        "checkin",
                        "checkout"
                    ],
                    "additionalProperties": true,
                    "properties": {
                        "checkin": {
                            "type": "string"
                        },
                        "checkout": {
                            "type": "string"
                        }
                    }
                },
                "additionalneeds": {
                    "type": "string"
                }
            }
        }
    }
}