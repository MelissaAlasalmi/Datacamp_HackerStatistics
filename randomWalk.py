import numpy as np 
import matplotlib.pyplot as plt

random_walk = [0]
np.random.seed(123)

for x in range(100) :
    step = random_walk[x]
	print("step before roll :" + str(step))
    dice = np.random.randint(1,7)
    print("dice: " + str(dice))
    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)
    random_walk.append(step)
	print("step after roll :" + str(step))
plt.plot(random_walk)
plt.show()