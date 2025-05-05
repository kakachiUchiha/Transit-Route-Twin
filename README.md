# Transit-Route Twin

![Node.js](https://img.shields.io/badge/Node.js-12.x-brightgreen)
![MIT License](https://img.shields.io/badge/License-MIT-blue)
![GitHub Repo](https://img.shields.io/badge/Repo-GitHub-blue)

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

**Transit-Route Twin** is a lightweight service that simulates live bus arrivals and delays by polling a public transit API, storing the results in real time, and broadcasting updates via WebSockets.

Originally built for the Transport for London (TfL) Live Bus Arrivals API, it can be easily adapted for any city's transit system.

---

## Features

- 🚍 **Real-Time Polling**: Periodically fetches next-bus ETAs for a given route.
- 📡 **WebSocket Broadcasting**: Instantly pushes updates to all connected clients.
- 🗺️ **Flexible Frontend**: Renders interactive maps or timelines using JavaScript.
- 🧩 **Modular Design**: Clean separation of polling, storage, and rendering logic.
- 💡 **Lightweight**: Minimal resource usage, standardized JSON, no special hardware required.

---

## Architecture

+-----------+ +------------+ +----------------+
| Polling | --> | Real-Time | --> | WebSocket |
| Service | | Store | | Broadcaster |
+-----------+ +------------+ +----------------+
|
v
Frontend (JS)

Map View

Timeline View



---

## Installation

### Clone the repository:

```bash
git clone https://github.com/youruser/transit-route-twin.git
cd transit-route-twin
```

### Install dependencies:

Backend (Node.js):
```bash
cd server
npm install
```
Frontend:
```bash
cd ../client
npm install
```
---
## Configuration
Copy .env.example in the server/ directory and rename it to .env, then update the values:

```env

TFL_APP_ID=your_tfl_app_id
TFL_APP_KEY=your_tfl_app_key
POLL_INTERVAL_MS=10000
PORT=3000
API_BASE_URL=https://api.tfl.gov.uk/Line/{lineId}/Arrivals
```
Replace with actual credentials and API endpoints for your city if not using TfL.
---
## Usage
Start the backend:
```bash
cd server
npm start
```
Start the frontend:
```bash
cd ../client
npm start
```
Open your browser at: http://localhost:8080
---
## API Reference
```bash
GET /route/:lineId/arrivals
Fetches the latest estimated bus arrivals for a given route.
```
Sample Response:
```json

[
  {
    "vehicleId": "1234",
    "lineId": "25",
    "destinationName": "Oxford Circus",
    "expectedArrival": "2025-05-05T15:32:00Z",
    "timeToStation": 240
  }
]
```
---
## How It Works
### 🔁 Polling Service
Sends periodic GET requests to:

```arduino

https://api.tfl.gov.uk/Line/{lineId}/Arrivals
```
Parses and normalizes the JSON response.
### 🧠 Real-Time Store
Maintains an in-memory (or Redis-based) store of predictions. Emits updates only when data changes.

### 📢 WebSocket Broadcaster
Broadcasts updated data to all subscribed clients. Each client can subscribe to specific lineIds.

### 🖥️ Frontend Renderer
Connects to the WebSocket server and dynamically renders:

Map View: Buses shown as map markers.

Timeline View: Horizontal timeline of expected arrivals.

---
## Contributing
Contributions are welcome!

1. Fork the repository

2. Create your feature branch:

```bash

git checkout -b feature/my-feature
```
3. Commit your changes:

```bash

git commit -am 'Add my feature'
```
4. Push to the branch:
```bash
git push origin feature/my-feature
```
5. Open a Pull Request

---
### License
MIT License © SFAXI Mohamed Khalil

### Badges Breakdown:
1. **Node.js Badge**: Shows the supported Node.js version.
2. **MIT License Badge**: Indicates the license under which the project is released.
3. **GitHub Repo Badge**: Quick access to the GitHub repository.
