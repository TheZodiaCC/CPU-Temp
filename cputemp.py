import time

file = "/sys/class/thermal/thermal_zone0/temp"

while True:
    with open(file) as data:
        print(f"{(data.read())[:2]}°C")
    time.sleep(3)