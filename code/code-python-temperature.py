import paho.mqtt.client as mqtt   # MQTT : protocole de messagerie pour l'IoT
                                    # Permet d'envoyer les données du capteur à Node-RED

import time                         # Gestion du temps et des pauses
                                    # Utilisé pour attendre entre deux lectures du capteur

import board                        # Définition des broches GPIO (Adafruit)
                                    # Fournit les noms des broches : D4, D17, D18...

import adafruit_dht                 # Pilote du capteur DHT22
                                    # Permet de lire la température 
# CONFIGURATION DU CAPTEUR DHT22

# DHT22 sur GPIO4 (Pin 7 physique du Raspberry Pi)
dht_device = adafruit_dht.DHT22(board.D4)
                                    # Crée l'objet capteur sur la broche GPIO4

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
                                    # Crée un client MQTT (version 2 de l'API)

client.connect("localhost", 1883)
                                    # Se connecte à Mosquitto sur le même Pi
                                    # localhost = 127.0.0.1 (machine locale)
                                    # 1883 = port standard MQTT

print("📡 Capteur DHT22 démarré...")
while True:
    try:

        temperature = dht_device.temperature
                                    # Lit la température réelle du capteur
                                    # Retourne un float (ex: 26.8473)
                                    # Peut retourner None si échec

        # TRAITEMENT ET ENVOI DES DONNÉES

        if temperature is not None:
                                    # Vérifie que la lecture a réussi

            temp_rounded = round(temperature, 1)
                                    # ARRONDI à 1 chiffre après la virgule

            client.publish("capteur/temperature", temp_rounded)
                                    # Envoie la valeur arrondie au broker MQTT
                                    # Topic : "capteur/temperature"
                                    # Node-RED reçoit cette valeur en temps réel

            print(f"📤 Température : {temp_rounded} °C")
                                    # Affiche dans le terminal (optionnel)

        else:
            print("⚠️ Lecture DHT22 échouée")
                                    # Le capteur n'a pas répondu cette fois
except RuntimeError as error:
                                    # Gestion des erreurs du DHT22
                                    # Le capteur est capricieux (checksum, timing)

        print(f"⚠️ Erreur DHT22 : {error.args[0]}")
                                    # Affiche l'erreur sans planter le programme

    time.sleep(3)
                                    # Attend 3 secondes avant de relire
                                    # Le DHT22 a besoin de temps pour se stabiliser
                                    # Trop rapide = erreurs fréquentes

