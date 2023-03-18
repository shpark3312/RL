from util import *
import numpy as np

state_val = np.zeros(maze.shape)
state_pol = np.full(maze.shape,None)

for (r,c), x in np.ndenumerate(maze):
    if x == 1: continue
    state_pol[r,c] = 'left'

p = 0.02
gamma = 0.95
theta = 0.01
start = np.array([15,4])

action = -1
oil = -5
bump = -10
goal = 200

Agent = Agent(start_loc=start,stochasticity=p)

def reward(r,c):
    if maze[r,c] == 1: return 0
    r = 0
    if maze[r,c] == 2:
        r += bump
    if maze[r,c] == 3:
        r += oil
    if maze[r,c] == 5:
        r += goal
    r += action
    return r

def update_state_val(state_val,r,c):
    if maze[r,c] == 1: return 0
    
    act_right = ((1-p)*(reward(r,c+1)+gamma*state_val[r,c+1]) 
                +(p/3)*(reward(r+1,c)+gamma*state_val[r+1,c])
                +(p/3)*(reward(r,c-1)+gamma*state_val[r,c-1])
                +(p/3)*(reward(r-1,c)+gamma*state_val[r-1,c])) 
    
    act_left =  ((p/3)*(reward(r,c+1)+gamma*state_val[r,c+1]) 
                +(p/3)*(reward(r+1,c)+gamma*state_val[r+1,c])
                +(1-p)*(reward(r,c-1)+gamma*state_val[r,c-1])
                +(p/3)*(reward(r-1,c)+gamma*state_val[r-1,c])) 
    
    act_up =    ((p/3)*(reward(r,c+1)+gamma*state_val[r,c+1]) 
                +(p/3)*(reward(r+1,c)+gamma*state_val[r+1,c])
                +(p/3)*(reward(r,c-1)+gamma*state_val[r,c-1])
                +(1-p)*(reward(r-1,c)+gamma*state_val[r-1,c])) 
    
    act_down =  ((p/3)*(reward(r,c+1)+gamma*state_val[r,c+1]) 
                +(1-p)*(reward(r+1,c)+gamma*state_val[r+1,c])
                +(p/3)*(reward(r,c-1)+gamma*state_val[r,c-1])
                +(p/3)*(reward(r-1,c)+gamma*state_val[r-1,c])) 
    
    if state_pol[r,c] == 'left' : return act_left
    if state_pol[r,c] == 'right' : return act_right
    if state_pol[r,c] == 'up' : return act_up
    if state_pol[r,c] == 'down' : return act_down

def pol_eval(delta=100):
    i=0
    while delta > theta:
        delta = 0
        for (r,c), x in np.ndenumerate(maze):
            if x == 1: continue
            v = state_val[r,c]
            state_val[r,c] = update_state_val(state_val,r,c)
            delta = np.maximum(delta,abs(v - state_val[r,c]))
        i=i+1
        print(delta,i)

pol_stable = True

for (r,c), x in np.ndenumerate(maze):
    if x == 1: continue
    old_act = state_pol[r,c]
    # update state_pol
    if old_act!=state_pol[r,c]: 
        pol_stable=False
        break
    



