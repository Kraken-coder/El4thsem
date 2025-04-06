from gpiozero import AngularServo
from time import sleep

servo = AngularServo(12, 
                     min_angle=-90, 
                     max_angle=90, 
                     min_pulse_width=0.0005, 
                     max_pulse_width=0.0025)

def get_current_angle():
    return servo.angle if servo.angle is not None else 0

def move_servo_to_angle(target_angle):
    current_angle = get_current_angle()
    target_angle = max(-90, min(90, target_angle))

    step = 1 if target_angle > current_angle else -1
    for angle in range(int(current_angle), int(target_angle + step), step):
        servo.angle = angle
        sleep(0.01)  # smaller sleep = smoother but slower

try:
    print(4)
    
    sleep(1)

    for i in [-90]:
        print(f"here ist is hehjb {i}")
        try:
            move_servo_to_angle(i)
            sleep(0.4)
    
        finally:
            continue
        

finally:
    print(5)
    servo.detach()
