import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
import time


# initializing the pin numbers where motors are connected
L_PWM_PIN1 = 33
L_PWM_PIN2 = 32
ENA = 31
ENB = 37
R_PWM_PIN2 = 40
R_PWM_PIN1 = 38





 
# declare motor pins as output pins
# motors get input from the PWM pins
def motor_pin_setup():
    global L_MOTOR1, L_MOTOR2, R_MOTOR1, R_MOTOR2
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ENA,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(ENB,GPIO.OUT,initial = GPIO.HIGH)
    
    GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    GPIO.setup(R_PWM_PIN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(R_PWM_PIN2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(L_PWM_PIN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(L_PWM_PIN2, GPIO.OUT, initial=GPIO.LOW)
    

    # setting initial PWM frequency for all 4 pins
    L_MOTOR1 = GPIO.PWM(L_PWM_PIN1, 100) 
    R_MOTOR1 = GPIO.PWM(R_PWM_PIN1, 100)
    L_MOTOR2 = GPIO.PWM(L_PWM_PIN2, 100)
    R_MOTOR2 = GPIO.PWM(R_PWM_PIN2, 100) 
    
    
    
    
    
    # setting initial speed (duty cycle) for each pin as 0
    L_MOTOR1.start(0)
    R_MOTOR1.start(0)
    L_MOTOR2.start(0)
    R_MOTOR2.start(0)
    
# function for moving forward
def forward(left, right):
    L_MOTOR1.ChangeDutyCycle(left)
    R_MOTOR1.ChangeDutyCycle(right)
    
# function for moving backward
def backward(left, right):
    R_MOTOR2.ChangeDutyCycle(left)
    L_MOTOR2.ChangeDutyCycle(right)
    
def right(left, right):
    R_MOTOR1.ChangeDutyCycle(left)
    L_MOTOR2.ChangeDutyCycle(right)
    
def left(left, right):
    R_MOTOR2.ChangeDutyCycle(left)
    L_MOTOR1.ChangeDutyCycle(right)

# function for pausing the motors
def motor_pause(secs,speed):
	time.sleep(secs)
	L_MOTOR1.ChangeDutyCycle(speed)
	R_MOTOR1.ChangeDutyCycle(speed)
	L_MOTOR2.ChangeDutyCycle(0)
	R_MOTOR2.ChangeDutyCycle(0)

# function for stopping both motors
def stop():
    L_MOTOR1.stop()
    R_MOTOR1.stop()
    L_MOTOR2.stop()
    R_MOTOR2.stop()
    GPIO.cleanup()





# capture frames from the camera

def ctrl(pin_no1,pin_no2,dist):
	stateLast1,stateLast2 = GPIO.input(pin_no1),GPIO.input(pin_no2)
	rotationCount1,rotationCount2 = 0,0
	stateCount1,stateCount2 = 0,0
	stateCountTotal1,stateCountTotal2 = 0,0
	flag = 0

	circ = 220 # mm
	statesPerRotation = 40
	distancePerStep = circ / statesPerRotation

	while True: # Use boolean logic not string evaluation
		stateCurrent1,stateCurrent2 = GPIO.input(pin_no1),GPIO.input(pin_no2)
		if stateCurrent1 != stateLast1:
			stateLast1 = stateCurrent1
			stateCount1 += 1
			stateCountTotal1 += 1
		if stateCurrent2 != stateLast2:
			stateLast2 = stateCurrent2
			stateCount2 += 1
			stateCountTotal2 += 1
		
		if stateCount1 == statesPerRotation:
			rotationCount1 += 1
			stateCount1 = 0
			
		if stateCount2 == statesPerRotation:
			rotationCount2 += 1
			stateCount2 = 0

		distance1 = distancePerStep * stateCountTotal1
		distance2 = distancePerStep * stateCountTotal2
		
		# print("Distance", distance)  # Do not print in th e loo
		
		if distance1>dist and distance2 > dist:
			return distance1,distance2


#def distance():

def m():
		
	forward(100,100)
	time.sleep(0.65)
	motor_pause(1)
	stop()

def m2():
	error = 4	
#print(ctrl(24,26,20))

	fs = 100

	motor_pin_setup()
	forward(fs,fs)
	time.sleep(0.5)
	motor_pause(0.5)
	forward(0.9*fs,fs)
	time.sleep(0.25)
	motor_pause(0.5)
	forward(fs,0.9*fs)
	#print(ctrl(24,26,320))
	#motor_pause(0.5)
	#left(75,75)
	#forward(100,75)
	#print(ctrl(24,26,100))
	time.sleep(0.5)
	motor_pause(0.5)
	stop()

