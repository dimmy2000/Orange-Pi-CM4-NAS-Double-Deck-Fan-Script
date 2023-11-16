#!/usr/bin/python3
from time import sleep

import wiringpi
from wiringpi import GPIO

FAN_PIN = 23  # RPi CM4 GPIO pin 35
TEMP = 50  # lowest temperature to turn fan ON


def get_cpu_temperature():
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        temp_sensor_data = int(f.read())
    return temp_sensor_data / 1000

if __name__== '__main__':
    wiringpi.wiringPiSetup()
    wiringpi.pinMode(FAN_PIN, GPIO.OUTPUT)

    while True:
        temp = get_cpu_temperature()
        print("The temp is %f" % temp)
        print("\33[3A")
        # Turn fan ON if CPU temperature is bigger than TEMP const
        if temp >= TEMP:
            # turn fan ON
            wiringpi.digitalWrite(FAN_PIN, GPIO.HIGH)
        else:
            # turn fan OFF
            wiringpi.digitalWrite(FAN_PIN, GPIO.LOW)
        sleep(10)
