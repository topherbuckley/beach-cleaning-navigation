import time
import math
import Jetson.GPIO as GPIO


def main():
    pwm_pins = [32,33]
    # Pin Setup:
    # Board pin-numbering scheme
    GPIO.setmode(GPIO.BOARD)

    _frequency_hz = 50
    _duty_cycle_percent = 25
    incr = 5

    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(pwm_pins[0], GPIO.OUT, initial=GPIO.HIGH)
    # p1 is a PWM object.
    p1 = GPIO.PWM(pwm_pins[0], _frequency_hz)
    p1.start(_duty_cycle_percent)
    # set pin as an output pin with optional initial state of HIGH
    # Note this setup cannot be combined by passing the whole array
    # as indicated in the NVDIA README
    # See: https://forums.developer.nvidia.com/t/unable-to-get-multiple-pwm-pins-to-work-simultaneously/284049
    GPIO.setup(pwm_pins[1], GPIO.OUT, initial=GPIO.HIGH)
    p2 = GPIO.PWM(pwm_pins[1], _frequency_hz)
    p2.start(_duty_cycle_percent)

    print("PWM running. Press CTRL+C to exit.")
    try:
        while True:
            time.sleep(0.25)
            if _duty_cycle_percent >= 100:
                incr = -incr
            if _duty_cycle_percent <= 0:
                incr = -incr
            _duty_cycle_percent += incr
            p1.ChangeDutyCycle(_duty_cycle_percent)
            p2.ChangeDutyCycle(_duty_cycle_percent)
    finally:
        p1.stop()
        p2.stop()
        GPIO.cleanup()

if __name__ == '__main__':
    main()
