import numpy as np 

# Which step you are on in a building
step = 50

# Roll a simulated dice
dice = np.random.randint(6, 7)
print("dice roll: " + str(dice))

# factor the roll into outcome
if dice <= 2 :
    step = step - 1
elif dice >= 3 and dice <= 5 :
    step = step + 1
else :
    reroll = np.random.randint(1, 7)
    step = step + reroll 
    print("reroll: " + str(reroll))
print("steps after round: " + str(step))