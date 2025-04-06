from gpiozero import Motor
from time import sleep

# Initialize the two motors with their corresponding GPIO pins.
# Left motor: forward on GPIO 17, backward on GPIO 22.
motor_left = Motor(forward=17, backward=22)

# Right motor: forward on GPIO 23, backward on GPIO 24.
motor_right = Motor(forward=23, backward=24)

def forward(sec):
    """Drive both motors forward for the given number of seconds."""
    motor_left.forward()
    motor_right.forward()
    sleep(sec)
    motor_left.stop()
    motor_right.stop()

def reverse(sec):
    """Drive both motors in reverse for the given number of seconds."""
    motor_left.backward()
    motor_right.backward()
    sleep(sec)
    motor_left.stop()
    motor_right.stop()

if __name__ == "__main__":
    print("Moving forward")
    forward(4)
    print("Moving reverse")
    reverse(2)


# orange - 17 - brown
# yellow - 22 red
# green 23 purple
# black 24 black-