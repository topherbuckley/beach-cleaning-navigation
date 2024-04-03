import time
import math
import Jetson.GPIO as GPIO
from beachbot.manipulators import Motor


def main():
    pwm_pins = [32, 33]
    gpio_pins = [7, 15, 29, 31]
    _frequency_hz = 50

    GPIO.setmode(GPIO.BOARD)

    motor1 = Motor(pwm_pins[0], gpio_pins[0], gpio_pins[1], _frequency_hz)
    motor2 = Motor(pwm_pins[1], gpio_pins[2], gpio_pins[3], _frequency_hz)

    speed = 0
    incr = 10  # Increment by 10 for each step
    max_speed = 100

    print("PWM running. Press CTRL+C to exit.")
    try:
        while True:
            time.sleep(0.1)
            if speed >= max_speed:
                incr = -incr
            if speed <= -max_speed:
                incr = -incr

            speed += incr
            print(f"speed post update: {speed}")

            motor1.change_speed(speed)
            motor2.change_speed(speed)
    finally:
        motor1.turn_off()
        motor2.turn_off()
        GPIO.cleanup()


if __name__ == "__main__":
    main()
