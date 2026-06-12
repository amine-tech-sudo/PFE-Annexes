import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

# CHOIX ICI : True = durée, False = immédiat
MODE_DUREE = False       # ← Change ici !
DUREE_SECONDES = 5      # ← Secondes si MODE_DUREE = True

GPIO.setmode(GPIO.BCM)

POMPE_PIN = 20
VENTILATEUR_PIN = 18
BUZZER_PIN = 27

GPIO.setup(POMPE_PIN, GPIO.OUT)
GPIO.setup(VENTILATEUR_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

GPIO.output(POMPE_PIN, GPIO.HIGH)
GPIO.output(VENTILATEUR_PIN, GPIO.HIGH)
GPIO.output(BUZZER_PIN, GPIO.LOW)

pwm_buzzer = GPIO.PWM(BUZZER_PIN, 1000)
pwm_buzzer.start(0)

buzzer_timer = 0
def on_message(client, userdata, message):
    global buzzer_timer

    topic = message.topic
    payload = message.payload.decode()

    if topic == "actionneur/pompe":
        if payload == "ON":
            GPIO.output(POMPE_PIN, GPIO.HIGH)
            print("💧 POMPE → ON")
        else:
            GPIO.output(POMPE_PIN, GPIO.LOW)
            print("💧 POMPE → OFF")

    elif topic == "actionneur/ventilateur":
        if payload == "ON":
            GPIO.output(VENTILATEUR_PIN, GPIO.HIGH)
            print("🌀 VENTILATEUR → ON")
        else:
            GPIO.output(VENTILATEUR_PIN, GPIO.LOW)
            print("🌀 VENTILATEUR → OFF")

    elif topic == "actionneur/buzzer":
        if payload == "ON":
            pwm_buzzer.ChangeDutyCycle(50)

            if MODE_DUREE:
                 # Mode durée : ignorer OFF, timer gère l'arrêt
                print("🔔 BUZZER → OFF ignoré (timer actif)")
            else:
                # Mode immédiat : arrêter maintenant
                pwm_buzzer.ChangeDutyCycle(0)
                buzzer_timer = 0
                print("🔔 BUZZER → OFF (immédiat)")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message
client.connect("localhost", 1883)
client.subscribe("actionneur/pompe")
client.subscribe("actionneur/ventilateur")
client.subscribe("actionneur/buzzer")

print("🎛️ Actionneurs démarrés..." )
print(f"Mode buzzer: {'DURÉE ' + str(DUREE_SECONDES) + 's' if MODE_DUREE else 'IMMÉDIAT'}")

try:
    while True:
        client.loop(timeout=0.1)

        # Timer seulement en mode durée
        if MODE_DUREE and buzzer_timer > 0 and time.time() > buzzer_timer:
            pwm_buzzer.ChangeDutyCycle(0)
            buzzer_timer = 0
            print("🔔 BUZZER → OFF (fin durée)")
            except KeyboardInterrupt:
    pwm_buzzer.stop()
    GPIO.cleanup()
    print("Arrêt propre")
