
import json
from machine import UART

# https://www.engineersgarage.com/micropython-esp8266-esp32-uart/

uart_port = 2
uart = UART(uart_port, baudrate=9600)

print(f"Waiting on input from UART {uart_port}...")
while True:
    res = uart.read()

    if res is not None:
        try:
            out = json.loads(res)
            print(f"Received: {out}")
            break
        except Exception as err:
            print(f"Error decoding packet: {res}")
            print(str(err))
print(res)
