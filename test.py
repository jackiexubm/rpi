import RPi.GPIO as GPIO
import time
from threading import Thread

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

def rotate(motor, angle):
    def _helper():
        n_steps = int(angle / 360.0 * 512)
        for i in range(n_steps):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(motor[pin], seq[halfstep][pin])
                time.sleep(0.001)
                print(i)
    # use threads to make rotations asynchronous
    Thread(target=_helper).start()

try:
    rotate(motor1, 360)
    rotate(motor2, 360)

except KeyboardInterrupt:
    raise
except:
    GPIO.cleanup()

# GPIO.cleanup()
