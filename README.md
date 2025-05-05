# Transit-Route Twin

Simulez les arrivées en temps réel et les retards de bus pour n’importe quel réseau de transport urbain.

---

## Table des matières

- [Présentation](#présentation)
- [Fonctionnalités](#fonctionnalités)
- [Architecture](#architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [API Reference](#api-reference)
- [Fonctionnement](#fonctionnement)
- [Contribuer](#contribuer)
- [Licence](#licence)

---

## Présentation

**Transit-Route Twin** est un service léger qui simule les arrivées et retards de bus en temps réel. Il interroge une API de transport public, stocke les résultats, puis diffuse les mises à jour en direct via WebSockets.

Initialement conçu pour l’API *Transport for London (TfL) Live Bus Arrivals*, il peut facilement être adapté à n’importe quel réseau de transport urbain.

---

## Fonctionnalités

- **Interrogation en temps réel** : récupère régulièrement les ETA (Estimated Time of Arrival) des bus pour une ligne donnée.
- **Diffusion WebSocket** : envoie instantanément les mises à jour aux clients connectés.
- **Frontend flexible** : rend des cartes interactives ou des timelines en JavaScript.
- **Architecture modulaire** : séparation des couches de polling, de stockage et d'affichage.
- **Léger et simple** : une seule requête REST par ligne, réponses JSON standardisées.

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

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/youruser/transit-route-twin.git
   cd transit-route-twin
Installez les dépendances :

Backend (Node.js) :
cd server
npm install

Frontend :
cd ../client
npm install
Ouvrez ensuite votre navigateur à l’adresse :
http://localhost:8080 (ou le port configuré)

API Reference
GET /route/:lineId/arrivals
Renvoie la liste des arrivées de bus estimées pour une ligne donnée.

Réponse :

json
Copier
Modifier
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
Fonctionnement
Polling Service
Envoie régulièrement des requêtes GET à l’API TfL :

arduino
Copier
Modifier
https://api.tfl.gov.uk/Line/{lineId}/Arrivals
Les données JSON sont ensuite normalisées.

Real-Time Store
Maintient un stockage en mémoire (ou Redis) des dernières prédictions.
Émet des mises à jour uniquement en cas de changement réel.

WebSocket Broadcaster
Diffuse les mises à jour vers tous les clients abonnés à un ou plusieurs lineId.

Frontend Renderer
Se connecte au serveur WebSocket et affiche les données :

Vue Carte : emplacements des bus en approche.

Vue Timeline : chronologie horizontale des prochaines arrivées.

Contribuer
Les contributions sont les bienvenues !

Forkez le dépôt

Créez une branche (git checkout -b feature/ma-feature)

Commitez vos modifications (git commit -am 'Ajout de ma feature')

Poussez la branche (git push origin feature/ma-feature)

Ouvrez une pull request

Licence
MIT License © SFAXI Mohamed Khalil
