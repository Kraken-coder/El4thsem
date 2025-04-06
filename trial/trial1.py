from gpiozero import AngularServo
from time import sleep

# Create an AngularServo instance on GPIO 12.
# Adjust min_angle, max_angle, min_pulse_width, and max_pulse_width as required.
servo = AngularServo(12, 
                      min_angle=-90, 
                      max_angle=90, 
                      min_pulse_width=0.0005,   # typically ~0.5ms
                      max_pulse_width=0.0025)   # typically ~2.5ms

try:
    # Sweep smoothly from -90° to +90°
    for angle in range(-90, 91, 2):  # 2° steps; adjust step size for smoother motion
        servo.angle = angle
        sleep(0.02)  # 20ms delay between steps (adjust for speed)
    
    # Sweep smoothly back from +90° to -90°
    for angle in range(90, -91, -2):
        servo.angle = angle
        sleep(0.02)
        
finally:
    # Detach the servo to stop sending PWM signals
    print("yghdijunyughdiunjniu")
    servo.detach()
