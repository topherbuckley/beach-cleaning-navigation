import time
import math
import Jetson.GPIO as GPIO


class Motor:
    def __init__(self, pwm_pin: int, in1: int, in2: int, _frequency_hz: int) -> None:
        self.pwm_pin: int = pwm_pin
        self.in1: int = in1
        self.in2: int = in2
        self._frequency_hz: int = _frequency_hz
        self._duty_cycle_percent: int = (
            0  # Initialized to 0, and int can hold -100 to 100 inclusively
        )
        # set pin as an output pin with optional initial state of LOW
        GPIO.setup(self.pwm_pin, GPIO.OUT, initial=GPIO.LOW)
        # p1 is a PWM object.
        self.pwm = GPIO.PWM(self.pwm_pin, self._frequency_hz)
        self.pwm.start(self._duty_cycle_percent)

    def change_speed(self, duty_cycle_percent: int) -> None:
        # I only add this as we may want to use it as a state variable later
        self._duty_cycle_percent = duty_cycle_percent
        self.pwm.ChangeDutyCycle(self._duty_cycle_percent)

    def turn_off(self) -> None:
        self.pwm.stop()


def main():
    pwm_pins = [32, 33]
    gpio_pins = [7, 15, 29, 31]
    _frequency_hz = 50

    # Board pin-numbering scheme
    GPIO.setmode(GPIO.BOARD)

    motor1 = Motor(pwm_pins[0], gpio_pins[0], gpio_pins[1], _frequency_hz)
    motor2 = Motor(pwm_pins[1], gpio_pins[2], gpio_pins[3], _frequency_hz)

    _duty_cycle_percent = 25
    incr = 5

    print("PWM running. Press CTRL+C to exit.")
    try:
        while True:
            time.sleep(0.25)
            if _duty_cycle_percent >= 100:
                incr = -incr
            if _duty_cycle_percent <= 0:
                incr = -incr
            _duty_cycle_percent += incr
            motor1.change_speed(_duty_cycle_percent)
            motor2.change_speed(_duty_cycle_percent)
    finally:
        motor1.turn_off()
        motor2.turn_off()
        GPIO.cleanup()


if __name__ == "__main__":
    main()
