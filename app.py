import random
import time

# Takes inputs

delay = input("What is the delay between generating new numbers?: ")
max = input("What is the max random number to generate?: ")


# Does the actual thing
time.sleep(2.5)
print("Started Generating Numbers")

while max <= max:
    time.sleep(float(delay))
    print(random.randint(1, int(max)))
