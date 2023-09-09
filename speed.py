import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(13, GPIO.OUT)  # clockwise left
GPIO.setup(15, GPIO.OUT)  # anticlockwise right
GPIO.setup(16, GPIO.OUT)  # anticlockwise left
GPIO.setup(18, GPIO.OUT)  # clockwise right

stateLast = GPIO.input(11)
rotationCount = 0
stateCount = 0
stateCountTotal = 0
flag = 0

circ = 62.4 * 3.14  # mm
statesPerRotation = 20
distancePerStep = circ / statesPerRotation

GPIO.output(13, GPIO.HIGH)
GPIO.output(18, GPIO.HIGH)
# flag = "true"

while True: # Use boolean logic not string evaluation
    stateCurrent = GPIO.input(11)
    if stateCurrent != stateLast:
        stateLast = stateCurrent
        stateCount += 1
        stateCountTotal += 1

    if stateCount == statesPerRotation:
        rotationCount += 1
        stateCount = 0

    distance = distancePerStep * stateCountTotal
    # print("Distance", distance)  # Do not print in th e loop
    if distance > 50:
        break
print("Distance", distance)
GPIO.output(13, GPIO.LOW)
GPIO.output(18, GPIO.LOW)
