import time
import sys

star = "*"

print(star, end ="")

for t in range(0,20):
    print (star, end = "", flush=True)
    time.sleep(0.1)       
