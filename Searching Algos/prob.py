dice_rolls = []

for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            dice_rolls.append((i, j, k))
            
sum_to_nine = [x for x in dice_rolls if sum(x)==9]

print(sum_to_nine)

print(len(sum_to_nine))