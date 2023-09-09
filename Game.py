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
def motor_pause(secs):
    L_MOTOR1.ChangeDutyCycle(0)
    R_MOTOR1.ChangeDutyCycle(0)
    L_MOTOR2.ChangeDutyCycle(0)
    R_MOTOR2.ChangeDutyCycle(0)
    time.sleep(secs)

# function for stopping both motors
def stop():
    L_MOTOR1.stop()
    R_MOTOR1.stop()
    L_MOTOR2.stop()
    R_MOTOR2.stop()
    GPIO.cleanup()

if __name__ == '__main__':
	opt = 'x'
	motor_pin_setup()
	while opt != 'q':
		opt = input()
		time.sleep(1)
		if opt == 'w':
			motor_pause(1)
			forward(75,75)
		elif opt == 's':
			motor_pause(1)
			backward(75,75)
		elif opt == 'a':
			motor_pause(1)
			left(25,25)
		elif opt == 'd':
			motor_pause(1)
			right(25,25)
		elif opt == 'x':
			motor_pause(1)
		else:
			motor_pause(1)
			stop()
			break
