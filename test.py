target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]


import math
uniqueFinishers = set()
stepsToFinish = []
num_cars = len(position)

# Find the number of steps to finish
for i in range(num_cars):
    finishTime = math.ceil((target - position[i])/speed[i])
    stepsToFinish.append(finishTime)

# If 'i' will catch up to 'j', remove 'i' from finishers
for i in range(num_cars):
    for j in range(num_cars):
        if position[i] < position[j] and stepsToFinish[i] >= stepsToFinish[j]:
            print(i)
            uniqueFinishers.remove(i)
            
print(uniqueFinishers)