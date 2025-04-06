from gpiozero import AngularServo
from time import sleep

class DualServoController:
    def __init__(self, pin1, pin2,
                 min_angle=-90, max_angle=90,
                 min_pulse_width=0.0005, max_pulse_width=0.0025,
                 frame_width=0.02):
        """
        Initialize the controller with two servo pins tailored for MG90S servos.
        
        :param pin1: GPIO pin number for the first servo.
        :param pin2: GPIO pin number for the second servo.
        :param min_angle: Minimum angle (default 0° for MG90S).
        :param max_angle: Maximum angle (default 180° for MG90S).
        :param min_pulse_width: Minimum pulse width (default 0.0005 seconds).
        :param max_pulse_width: Maximum pulse width (default 0.0025 seconds).
        :param frame_width: Pulse train period, default 0.02 seconds (20 ms).
        """
        self.servo1 = AngularServo(pin1,
                                   min_angle=min_angle,
                                   max_angle=max_angle,
                                   min_pulse_width=min_pulse_width,
                                   max_pulse_width=max_pulse_width,
                                   frame_width=frame_width)
        self.servo2 = AngularServo(pin2,
                                   min_angle=min_angle,
                                   max_angle=max_angle,
                                   min_pulse_width=min_pulse_width,
                                   max_pulse_width=max_pulse_width,
                                   frame_width=frame_width)

    def move_to_angles(self, target_angle1, target_angle2, steps=50, delay=0.02):
        """
        Smoothly move both servos to the target angles using easing.
        
        :param target_angle1: Target angle for servo1.
        :param target_angle2: Target angle for servo2.
        :param steps: Number of incremental steps for the easing transition.
        :param delay: Delay in seconds between steps.+
        """
        # Default to center (90°) if no angle has been set yet
        current_angle1 = self.servo1.angle if self.servo1.angle is not None else 90
        current_angle2 = self.servo2.angle if self.servo2.angle is not None else 90

        # Calculate the difference between the current and target angles
        delta1 = target_angle1 - current_angle1
        delta2 = target_angle2 - current_angle2

        # Smoothstep easing: ease = t*t*(3-2*t)
        for step in range(1, steps + 1):
            t = step / steps
            ease = t * t * (3 - 2 * t)
            new_angle1 = current_angle1 + delta1 * ease
            new_angle2 = current_angle2 + delta2 * ease

            self.servo1.angle = new_angle1
            self.servo2.angle = new_angle2

            sleep(delay)

if __name__ == "__main__":
    # Initialize the DualServoController for MG90S servos on GPIO pins 17 and 27.
    controller = DualServoController(17, 27)

    # Move servos to extreme positions:
    # Servo1 to 0° and Servo2 to 180°.
    print("Moving servo1 to 0° and servo2 to 180°.")
    controller.move_to_angles(0, 0)
    sleep(1)

    # Move both servos back to center (90°).
    print("Moving both servos back to center (90°).")
    controller.move_to_angles(80, 80)
