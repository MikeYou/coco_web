import board
import digitalio
import busio

"""controlling servo mode PCA9685"""
from adafruit_servokit import ServoKit

"""controlling servo mode PCA9685"""

print("Hello blinka!")

# Try to great a Digital input
pin = digitalio.DigitalInOut(board.D4)
print("Digital IO ok!")

# Try to create an I2C device
i2c = busio.I2C(board.SCL, board.SDA)
print("I2C 1 ok!")
i2c = busio.I2C(board.SCL_1, board.SDA_1)
print("I2C 2 ok!")

print("done!")
# for 1st Motor on ENA
#ENA = D13 #33
#IN1 = D19#35
#IN2 = D26#37
#IN3 = D16#36
#IN4 = D20#38
#ENB = D12#32

import time

ENA = digitalio.DigitalInOut(board.D13)
IN1 = digitalio.DigitalInOut(board.D19)
IN2 = digitalio.DigitalInOut(board.D26)
IN3 = digitalio.DigitalInOut(board.D16)
IN4 = digitalio.DigitalInOut(board.D20)
ENB = digitalio.DigitalInOut(board.D12)

ENA.direction = digitalio.Direction.OUTPUT
IN1.direction = digitalio.Direction.OUTPUT
IN2.direction = digitalio.Direction.OUTPUT
IN3.direction = digitalio.Direction.OUTPUT
IN4.direction = digitalio.Direction.OUTPUT
ENB.direction = digitalio.Direction.OUTPUT

#initial
ENA.value = False
ENB.value = False
IN1.value = False
IN2.value = False
IN3.value = False
IN4.value = False


#start conveyor
ENA.value = True

IN1.value = 0
IN2.value = 1
#start rotate
#ENA.value = True

#IN1.value = 1
#IN2.value = 0


"""controlling servo mode PCA9685"""

kit = ServoKit(channels=16)
"""controlling servo mode PCA9685"""
kit.servo[8].angle=90
kit.servo[0].angle=90
a = input("stop? (y/n)")
if a == "y":
# Stop
    kit.servo[8].angle=90
    kit.servo[0].angle=90
    ENA.value = False
    ENB.value = False
    IN1.value = False
    IN2.value = False
    IN3.value = False
    IN4.value = False
    time.sleep(1)
    GPIO.cleanup()
else:
    pass


