The "agents" referred to here are ESP32-WROOM boards which perform the majority of the sensor I/O. 

Each of the batteries has a temperature sensor monitoring it, and the chassis has various LEDs and LCDs that are wired to the agents. 

There is a Lower Agent, in the main body, as well as an Upper Agent, which is in the rotating dome. 

Each of these agents is connected to the main board via I2C. They speak a universal protocol which embeds status messages in json.

The agents run Micropython.
