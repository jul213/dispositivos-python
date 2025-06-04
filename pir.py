from gpiozero import MotionSensor
from time import sleep

pir = MotionSensor(4)

while True:
    pir.wait_for_motion()
    print("movimiento detectado")
    pir.wait_for_no_motion()
    print("sin movimiento...")
