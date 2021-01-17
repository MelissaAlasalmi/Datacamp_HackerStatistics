import numpy as np 

# a coin is thrown for 10 throws, results recorded in a list
np.random.seed(123)
outcomes = []
for x in range(10) :
	coin = np.random.randint(0, 2)
	if coin == 0 :
		outcomes.append("heads")
	else :
		outcomes.append("tails")
print(outcomes)

# number of times tails is thrown for 10 throws recorded in a list
np.random.seed(567)
tails = [0]
for x in range(10) :
	coin = np.random.randint(0, 2)
	tails.append(tails[x] + coin)
print(tails)