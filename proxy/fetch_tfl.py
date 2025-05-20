
import requests
import json

# TfL API endpoint to replace with credientials
url = "https://api.tfl.gov.uk/StopPoint/490008660N/Arrivals"

response = requests.get(url)
arrivals = response.json()


entity = {
    "id": "BusStop-490008660N",
    "type": "BusStop",
    "name": {
        "value": "Shoreditch High Street",
        "type": "Text"
    },
    "arrivals": {
        "value": [
            {"line": bus['lineName'], "arrivalTime": bus['expectedArrival']}
            for bus in sorted(arrivals, key=lambda x: x['expectedArrival'])[:2]
        ],
        "type": "StructuredValue"
    },
    "timestamp": {
        "value": arrivals[0]['timestamp'],
        "type": "DateTime"
    }
}

print(json.dumps(entity, indent=2))
