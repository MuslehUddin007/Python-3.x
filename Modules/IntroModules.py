import math
import random
import time
import datetime
from datetime import date

print("Sqrt : ",math.sqrt(25))
print("Degrees : ",math.degrees(2))
print("Pi : ",math.pi)
print("Sin : ",math.sin(2))
print("Cos : ",math.cos(0.5))
print("Tan : ",math.tan(0.23))
print("Factorial : ",math.factorial(4))

print("Randint : ",random.randint(0,5))
print("Random : ",random.random())
print("Random * 100 : ",random.random() * 100)
List = [1,4,True,800,"python",27,"hello"]
print("Random Choice : ",random.choice(List))

print("Time : ",time.time())
print("Date : ",date.fromtimestamp(454554))