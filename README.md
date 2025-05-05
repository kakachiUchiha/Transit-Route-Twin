# Transit-Route Twin

Simulate real-time bus arrivals and delays for any city’s transit system.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Reference](#api-reference)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**Transit-Route Twin** is a lightweight service that simulates live bus arrivals and delays by polling a public transit API, storing results in real-time, and broadcasting updates over WebSockets.

Originally built for the Transport for London (TfL) Live Bus Arrivals API, it can be easily adapted to any city’s transit system.

---

## Features

- **Real-Time Polling**: Periodically fetches next-bus ETAs for a given route.
- **WebSocket Broadcasting**: Pushes updates to all connected clients instantly.
- **Flexible Frontend**: Renders interactive maps or timelines using JavaScript.
- **Modular Design**: Clean separation of polling, storage, and rendering logic.
- **Lightweight**: Minimal resource usage, standardized JSON, no specialized hardware.

---

## Architecture

+-------------+ +--------------+ +----------------+
| Polling | ---> | Real-Time | ---> | WebSocket |
| Service | | Store | | Broadcaster |
+-------------+ +--------------+ +----------------+
|
v
Frontend (JS)
(Map View / Timeline View)


---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/youruser/transit-route-twin.git
   cd transit-route-twin
2. Install dependencies:

Backend (Node.js):

cd server
npm install

Frontend:

bash
Copier
Modifier
cd ../client
npm install

---

## Configuration

Copy and customize the .env.example file inside the server/ directory:
TFL_APP_ID=your_tfl_app_id
TFL_APP_KEY=your_tfl_app_key
POLL_INTERVAL_MS=10000
PORT=3000
API_BASE_URL=https://api.tfl.gov.uk/Line/{lineId}/Arrivals

Replace the placeholder values with actual credentials or endpoints depending on your transit API provider.

---

## Usage
Start the backend:

bash
Copier
Modifier
cd server
npm start

Start the frontend:
cd ../client
npm start
Then open your browser at:
http://localhost:8080

---

## API Reference
GET /route/:lineId/arrivals
Fetch the latest list of estimated bus arrivals for a given route.

Response:
[
  {
    "vehicleId": "1234",
    "lineId": "25",
    "destinationName": "Oxford Circus",
    "expectedArrival": "2025-05-05T15:32:00Z",
    "timeToStation": 240
  },
  ...
]

---
## How It Works
### Polling Service
Sends periodic GET requests to the configured transit API:
https://api.tfl.gov.uk/Line/{lineId}/Arrivals

Parses and normalizes the JSON response.

### Real-Time Store
Maintains an in-memory or Redis-based store of active predictions.
Emits updates only when new data differs from the previous state.

### WebSocket Broadcaster
Broadcasts relevant data to all subscribed WebSocket clients.
Each client can subscribe to one or more lineIds.

### Frontend Renderer
Connects to the WebSocket server and dynamically renders:

Map View: Buses shown as markers on a map.

Timeline View: Horizontal timeline of upcoming arrivals.

---
## Contributing
Contributions are welcome!

1. Fork the repository

2. Create your feature branch
    git checkout -b feature/my-feature
3. Commit your changes
   git commit -am 'Add my feature'
4. Push to the branch
   git push origin feature/my-feature
5. Open a Pull Request

--- 
### License
MIT License © SFAXI Mohamed Khalil

