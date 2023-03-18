from util import *
import numpy as np
from matplotlib import pyplot as plt, colors, animation, patches


start = np.array([15,4])
num_step = 50
num_run = 500
data = []
p = 0.02
Agent = Agent(start, stochasticity=p)

for i in range(num_run):
    Agent.curr_loc = start
    Agent.reward_tot=0
    Agent.reward_hist=[]
    Agent.generate_rand_path(num_steps=num_step)
    data.append(Agent.reward_tot)

plt.hist(x=data,bins=50)
plt.title(f'Reward Distribution of {num_run} Independent Runs')

plt.show(block=False)
plt.pause(1)
print('Press enter to close the plot')
input()
plt.close()


