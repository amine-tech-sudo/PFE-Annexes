import paho.mqtt.client as mqtt
import time
import json
import RPi.GPIO as GPIO
import spidev

# === Configuration GPIO ===
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)  # DO du MQ-135 sur GPIO 17

# === Configuration SPI / MCP ===
spi = spidev.SpiDev()
spi.open(0, 0)  # Bus 0, CE0
spi.max_speed_hz = 1000000

def lire_ADC():
    """Lire la valeur analogique du  (12 bits, 0-4095)"""
    # MCP envoie 16 bits : 1 bit null + 12 bits de données + 3 bits vides
    r = spi.xfer2([0x00, 0x00])  # 2 octets = 16 bits
    # Reconstruction de la valeur 12 bits
    valeur = ((r[0] & 0x1F) << 8) | r[1]
    valeur = valeur >> 1  # Supprimer le bit null
    return valeur  # 0 à 4095

# === Configuration MQTT ===
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883)

print("💨 Capteur gaz MQ-135 démarré (DO  + AO  via ADC)...")

try:
    while True:
        # Lire DO (digital) depuis GPIO 17
        do = GPIO.input(17)

        # Lire AO (analogique) depuis MCP3201
        ao = lire_ADC()

        # Convertir en PPM approximatif (0-4095 → 0-1000 ppm)
        ppm = round((ao / 4095) * 1000, 2)

        # Préparer et envoyer les données MQTT
        data = json.dumps({"do": do, "ao": ao, "ppm": ppm})
        client.publish("capteur/gaz", data)

        # Affichage
        etat = "🔴 GAZ DÉTECTÉ !" if do == 0 else "✅ Normal"
        print(f"DO: {do} | AO brut: {ao}/4095 | PPM: {ppm} | {etat}")

        time.sleep(3)

except KeyboardInterrupt:
    print("\nArrêt...")

finally:
    spi.close()
    GPIO.cleanup()