import time
running = True
secondes = 0
end = 10 
while (running):
    print(secondes)
    time.sleep(1)
    secondes += 1
    if(secondes >= end):
        running = False
        print(secondes)
print("Time is UP!")