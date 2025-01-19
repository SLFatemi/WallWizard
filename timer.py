import time

running = True
secondes = 0
end = 8
while (running):
    print(secondes)
    time.sleep(1)
    secondes += 1

    if(secondes >= end):
        running = False
        print(secondes)

print("Time is UP!")
# this is a simple timer for the game altough it was not predicted
# so we do not need it until the game pushes a matter of time