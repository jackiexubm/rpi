import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

motor1 = [2, 3, 14, 15]
motor2 = [4, 18, 23, 24]

for pin in motor1:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

for pin in motor2:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

seq = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
]

try:
    for i in range(100):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(motor1[pin], seq[halfstep][pin])
            print(i)
            time.sleep(0.001)

    for j in range(100):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(motor2[pin], seq[halfstep][pin])
            print(i)
            time.sleep(0.001)

except KeyboardInterrupt:
    raise
except:
    GPIO.cleanup()

GPIO.cleanup()
