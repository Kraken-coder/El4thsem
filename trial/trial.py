
import RPi.GPIO as GPIO
import time
import pigpio
pi = pigpio.pi()
pi.set_servo_pulsewidth(17 , 1500)
servo_pin = 17  # Use GPIO 18 for PWM

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Set PWM frequency to 50Hz (standard for servos)
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(7.5)  # Neutral position (90 degrees)

def set_angle(angle):
    duty = 2.5 + (angle / 18)  # Convert angle to duty cycle
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)  # Give the servo time to move

try:
    while True:
        angle = int(input("Enter angle (0-180): "))
        set_angle(angle)
except KeyboardInterrupt:
    print("\nStopping...")
    pwm.stop()
    GPIO.cleanup()

	
