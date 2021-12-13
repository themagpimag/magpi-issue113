import RPi.GPIO as GPIO
import dht11

# intialise GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

while True:
    instance = dht11.DHT11(pin = 14)
    result = instance.read()
    if result.is_valid():
        print("Temperature: %-3.1f C" % result.temperature, "Humidity: %-3.1f %%" % result.humidity, end = "\r")
