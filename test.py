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

def clear(motor):
    for i in range(4):
        GPIO.output(motor[i], 0)
        GPIO.output(motor[i], 0)

def rotate(motor, angle):
    if (angle > 0):
        def _ccw():
            n_steps = int(angle / 360.0 * 512)
            for i in range(n_steps):
                for halfstep in range(8):
                    for pin in range(4):
                        GPIO.output(motor[pin], seq[halfstep][pin])
                    time.sleep(0.001)
            clear(motor)
        Thread(target=_ccw).start()
    else:
        def _cw():
            n_steps = int(angle * -1.0 / 360.0 * 512)
            print(n_steps)
            for i in range(n_steps):
                for halfstep in range(8):
                    for pin in range(4):
                        GPIO.output(motor[pin], seq[7 - halfstep][pin])
                    time.sleep(0.001)
            clear(motor)
        Thread(target=_cw).start()


try:
    rotate(motor1, 160)
    rotate(motor2, -160)

except KeyboardInterrupt:
    raise
except:
    pass
# GPIO.cleanup()
