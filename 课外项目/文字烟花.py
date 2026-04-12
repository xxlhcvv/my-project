import random
import time
import os

colors=['\033[91m','\033[93m','\033[92m','\033[94m','\03395m','033[96m']
reset='\033[0m'

words=["✨","hello","python","🎉", "Cool", "Fun", "Wow", "Yes!"]

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    for _ in range(10):
        x = random.randint(0, 50)
        y = random.randint(0, 20)
        c = random.choice(colors)
        w = random.choice(words)
        print("\n" * y + " " * x + c + w + reset)
    time.sleep(0.3)
