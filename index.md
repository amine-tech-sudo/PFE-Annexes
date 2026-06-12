---
layout: default
title: Annexes - PFE Système IoT 
---

# Annexes - PFE Système IoT 

## 📋 Informations du projet

| Élément | Détail |
|---------|--------|
| **Titre** | Conception et réalisation d'un système IoT intelligent de surveillance et de prévention des incendies et des gaz dangereux basé sur Raspberry Pi |
| **Date** | Juin 2025 |

---

## 💻 Code source

### Scripts Python des capteurs

| Fichier | Description | Lien |
|---------|-------------|------|
| [code-python-gaz.py](https://github.com/amine-tech-sudo/PFE-Annexes/blob/master/code-python-gaz.py) | Lecture du capteur MQ-135 | [Voir](https://github.com/amine-tech-sudo/PFE-Annexes/blob/master/code-python-gaz.py) |
| [code-python-flamme.py](https://github.com/amine-tech-sudo/PFE-Annexes/blob/master/code-python-flamme.py) | Lecture du capteur KY-026 | [Voir](https://github.com/amine-tech-sudo/PFE-Annexes/blob/master/code-python-flamme.py) |
| [code-python-temperature.py](https://github.com/amine-tech-sudo/PFE-Annexes/blob/master/code-python-temperature.py) | Lecture du capteur DHT22 | [Voir](https://github.com/amine-tech-sudo/PFE-Annexes/blob/master/code-python-temperature.py) |
| [code-python-actionneurs.py](https://github.com/amine-tech-sudo/PFE-Annexes/blob/master/code-python-actionneurs.py) | Commande des actionneurs via GPIO | [Voir](https://github.com/amine-tech-sudo/PFE-Annexes/blob/master/code-python-actionneurs.py) |

---

## 📚 Datasheets techniques

| Composant | Fichier | Source |
|-----------|---------|--------|
| Capteur DHT22 | [DHT22 datasheet.pdf](https://github.com/amine-tech-sudo/PFE-Annexes/blob/master/DHT22%20datasheet.pdf) | Adafruit Industries |
| Capteur MQ-135 | [MQ135 datasheet.PDF](https://github.com/amine-tech-sudo/PFE-Annexes/blob/master/MQ135%20datasheet.PDF) | Hanwei Electronics |
| Capteur KY-026 | [KY-026 datasheet.PDF](https://github.com/amine-tech-sudo/PFE-Annexes/blob/master/KY-026%20datasheet.PDF) | Keyes Studio |

---

## 🎥 Vidéo de démonstration

| Fichier | Description | Durée | Lien |
|---------|-------------|-------|------|
| [0612.mp4](https://github.com/amine-tech-sudo/PFE-Annexes/blob/master/0612.mp4) | Démonstration des flux Node-RED en fonctionnement | ~2 min | [Voir sur GitHub](https://github.com/amine-tech-sudo/PFE-Annexes/blob/master/0612.mp4) |

&gt; 📝 **Contenu de la vidéo** :
&gt; - Visualisation des flux de traitement des données
&gt; - Réception des messages MQTT des capteurs
&gt; - Déclenchement automatique des alertes
&gt; - Commande manuelle des actionneurs via Dashboard
&gt; - Historisation des données dans SQLite

---

## 📧 Contact

Pour toute question concernant ce projet :  
**Email** : aminelh2006@gmail.com