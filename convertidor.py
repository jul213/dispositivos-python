from gpiozero import MCP3008, PWMLED
from time import sleep

pot = MCP3008(channel=0)

led = PWMLED(18)