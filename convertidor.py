from gpiozero import MCP3008, PWMLED
from time import sleep

pot = MCP3008(channel=0)

led = PWMLED(18)

while True:
    led.value = pot.value
    print(f"valor potenciometro de: {pot.value:.2f}")
    sleep(0.1)