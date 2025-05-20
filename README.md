# 🚌 Transit-Route Twin – Digital Twin for Bus Arrival Simulation (TfL + FIWARE)

![Node.js](https://img.shields.io/badge/Node.js-12.x-brightgreen)
![MIT License](https://img.shields.io/badge/License-MIT-blue)
![GitHub Repo](https://img.shields.io/badge/Repo-GitHub-blue)

> A lightweight digital twin system that simulates real-time bus arrivals and delays in London by polling the TfL API, translating data to NGSI format, and storing it in FIWARE Orion Context Broker for visualization and consumption.
---
## Table of Contents

- [Contexte du Projet](#Contexte_du_Projet)
- [Architecture de la Solution](#Architecture_de_la_Solution)
- [Modèle de Données JSON (NGSI v2)](#Modèle_de_Données_JSON (NGSI v2))
- [Installation avec Docker Compose](#Installation_avec_Docker_Compose)
- [Lancer l'Application](#Lancer_l'Application)
- [Résultats](#Résultats)
- [Conclusion](#Conclusion)
- [Auteur](#Auteur)

---
## Contexte du Projet

Ce projet s’inscrit dans le cadre de l’exploration des **Digital Twins (Jumeaux Numériques)** appliqués aux systèmes de transport urbains intelligents.

L'objectif est de :
- Simuler en temps réel les **arrivées de bus** à un arrêt donné à Londres.
- Traduire ces données vers un format **NGSI v2** compatible avec FIWARE.
- Les stocker dans **Orion Context Broker**, une base de contexte dynamique.
- Visualiser ces données via des requêtes API (Postman/cURL) ou une interface frontale.

> 🏙️ Le Digital Twin ici représente un "reflet numérique" du réseau de transport de Londres, synchronisé avec les données temps réel du **Transport for London (TfL) API**.

---

## Architecture de la Solution


| composant de l'architecture        |Rôle                                                               |
|------------------------------------|-------------------------------------------------------------------|
| Orion Context Broker               | Cœur du jumeau numérique (stocke et diffuse le contexte en NGSI)  |
| MongoDB                            | Backend utilisé par Orion pour persister les entités              |
|NGSI Proxy                          | Connecte l’API TfL à Orion en traduisant les données              | 
|Postman / cURL                      | Tester les requêtes NGSI v2 vers Orion                            | 
|Frontend React                      | 	Affiche les arrivées de bus depuis Orion en temps réel           | 

---

## Modèle de Données JSON (NGSI v2)

Exemple d'entité envoyée à Orion :

```json
{
  "id": "BusStop-490008660N",
  "type": "BusStop",
  "name": {
    "value": "Shoreditch High Street",
    "type": "Text"
  },
  "arrivals": {
    "value": [
      { "line": "25", "arrivalTime": "2025-05-19T12:36:00Z" },
      { "line": "205", "arrivalTime": "2025-05-19T12:42:00Z" }
    ],
    "type": "StructuredValue"
  },
  "timestamp": {
    "value": "2025-05-19T12:30:00Z",
    "type": "DateTime"
  }
}
```
---
## Installation avec Docker Compose 
> Prérequis
[Docker](https://docs.docker.com/get-docker/)

[Docker Compose](https://docs.docker.com/compose/install/)
### Fichier docker-compose.yml
```yaml
version: "3.7"

services:
  orion:
    image: fiware/orion
    container_name: fiware-orion
    depends_on:
      - mongo
    ports:
      - "1026:1026"
    command: -dbhost mongo
    networks:
      - fiware

  mongo:
    image: mongo:4.4
    container_name: db-mongo
    ports:
      - "27017:27017"
    networks:
      - fiware

networks:
  fiware:
    driver: bridge
```

Ce fichier lance :
#### MongoDB : base de données pour stocker les entités de contexte.
#### Orion Context Broker : serveur de contexte NGSI.
---
## Lancer l'Application
### 1. Démarrer Orion et MongoDB
```bash
docker-compose up -d
```
### 2. Vérifier que Orion fonctionne
```bash
dcurl http://localhost:1026/version
```
### 3. Injecter des données simulées depuis TfL
Utilise un script Python ou cURL pour parser et transformer les données de TfL en JSON NGSI et les injecter dans Orion :
```bash
curl -iX POST \
  'http://localhost:1026/v2/entities' \
  -H 'Content-Type: application/json' \
  -H 'Fiware-Service: transit' \
  -H 'Fiware-ServicePath: /london' \
  -d @bus_stop_entity.json
```
Tu peux aussi utiliser Postman avec les mêmes headers pour tester l'API.

---
## Résultats 
###  Lecture d’une entité
```bash
curl -X GET \
  'http://localhost:1026/v2/entities/BusStop-490008660N?options=keyValues' \
  -H 'Fiware-Service: transit' \
  -H 'Fiware-ServicePath: /london'
```
#### Résultat :
```json
{
  "id": "BusStop-490008660N",
  "type": "BusStop",
  "name": "Shoreditch High Street",
  "arrivals": [
    { "line": "25", "arrivalTime": "2025-05-19T12:36:00Z" },
    { "line": "205", "arrivalTime": "2025-05-19T12:42:00Z" }
  ],
  "timestamp": "2025-05-19T12:30:00Z"
}
```
## Conclusion
Ce projet montre l’application concrète d’un jumeau numérique urbain, à l’aide d’un outil standard de gestion de contexte dynamique (Orion Context Broker). Il peut facilement être étendu à d’autres villes ou sources de données. Il respecte le paradigme Digital Twin : répliquer, suivre et comprendre un système physique à distance, en temps réel.

### Auteur
Projet réalisé dans le cadre du module “Digital Twin” 
Université SUP'COM 🇹🇳

