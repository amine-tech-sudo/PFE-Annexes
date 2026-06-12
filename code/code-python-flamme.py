import paho.mqtt.client as mqtt
import time
import json
import RPi.GPIO as GPIO
import spidev

# === Configuration GPIO ===
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# === Configuration SPI / MCP3201 ===
spi = spidev.SpiDev()
spi.open(0, 0)  # Bus 0, CE0
spi.max_speed_hz = 1000000

def lire_adc():
    r = spi.xfer2([0x00, 0x00])
    valeur = ((r[0] & 0x1F) << 8) | r[1]
    valeur = valeur >> 1
    return valeur  # 0 à 4095

# === Configuration MQTT ===
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883)

print("🔥 Capteur flamme JY-026 démarré (DO  + AO  via MCP)...")

try:
    while True:
        do_val = GPIO.input(24)
        ao = lire_adc()

        # Convertir en pourcentage (0-4095 → 0-100%)
        ao_pct = round((ao / 4095) * 100, 2)

        data = json.dumps({
            "do": do_val,
            "ao": ao,
            "ao_pct": ao_pct,
            "connected": True
        })
        client.publish("capteur/flamme", data)

        etat = "🔥 FLAMME" if do_val == 1 else "✅ Rien"
        print(f"DO:{do_val} | AO brut:{ao}/4095 | AO:{ao_pct}% | {etat}")

        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nArrêt")

finally:
    spi.close()
    GPIO.cleanup()