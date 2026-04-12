# Print a countdown before something “exciting” happens (like “Launching...” or
# “Happy New Year!”).

import time
count=int(input("Enter a number:"))

print("\n Count down start now...")

for i in range(count, 0, -1):
      print(i)
      time.sleep(1)

print("HAPPY NEW YEAR!")
print(i)
