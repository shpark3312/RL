from matplotlib import pyplot as plt, colors, animation, patches
import numpy as np
from draw_maze import *
from util import Agent

# 미로 환경에서 에이전트가 무작위 경로를 따라 이동하는 시각화를 만드는 코드
# 이 코드는 주어진 미로 환경에서 에이전트가 무작위로 이동하는 과정을 
# 시각화하는 데 도움이 됩니다. 그러나 최적의 경로나 정책을 찾는 것과는 
# 관련이 없습니다. 이 코드는 이전에 제공한 Policy Iteration 코드와 결합하여 
# 에이전트가 최적의 경로를 따라 이동하는 과정을 시각화할 수 있습니다.


# 무작위 경로 생성 
start = np.array([15,4]) # 초기 위치와 이동횟수 정의
num_step = 500
Agent = Agent(start,0.1)

# Agent.generate_rand_path(num_steps=num_step)
run_count = 0
while Agent.reward_tot < 10:
    Agent.reset(start_loc=start)
    Agent.generate_rand_path(num_steps=num_step)
    run_count=run_count+1


# 시각화 준비 빈 x,y 좌표 목록을 초기화
# 에이전트의 위치를 나타내는 원을 생성, 에이전트의 초기 위치로 설정
# 에이전트의 이동 단계와 보상을 나타내는 텍스트를 생성
# 에이전트의 경로를 추적하는 라인을 생성
xdata, ydata = [], [] 

# create a circle to denote position of agent
center = (Agent.path[0][1]+0.5,Agent.path[0][0]+0.5)
agent = patches.Circle(center,radius = 0.2)
agent.set(alpha = 0.40)
ax.add_patch(agent)

# text to show steps and reward
reward_str = ''
reward_txt = ax.text(0.5,1,reward_str, bbox={'facecolor': 'white'},
                verticalalignment='top', horizontalalignment='center',
                transform=ax.transAxes,)

# create a line to trace path taken
line, = ax.plot([], [], '--', lw=1, ms=2)
def init(): 
    line.set_data([], []) 
    return line,


# 초기화 함수 init는 라인 객체를 빈 상태로 설정합니다.
# 애니메이션 함수 animate는 다음을 수행합니다:
# 에이전트의 경로에서 x 및 y 좌표를 가져와 목록에 추가합니다.
# 라인의 데이터를 업데이트하여 에이전트의 경로를 표시합니다.
# 에이전트의 위치를 업데이트하고 알파 값을 설정합니다.
# 텍스트를 업데이트하여 현재 단계와 보상을 표시합니다.
def animate(i): 
    xdata.append(Agent.path[i][1]+0.5) 
    ydata.append(Agent.path[i][0]+0.5) 
    line.set_data(xdata, ydata) 
    agent.set(center=(xdata[i],ydata[i]))
    agent.set(alpha=1)
    if i < len(Agent.reward_hist): reward_str=(f'step: {i}, reward: {Agent.reward_hist[i]}')
    else: reward_str=(f'step: {i}, reward: {Agent.reward_hist[i-1]}, finished')
    reward_txt.set_text(reward_str)
    return line,agent,reward_txt


#시각화 출력:
# FuncAnimation 함수를 사용하여 애니메이션을 생성하고 시각화를 출력합니다.
# 애니메이션이 완료된 후, 무작위 경로를 생성하는 데 필요한 실행 횟수와 종료 메시지를 출력합니다.
anim = animation.FuncAnimation(fig, animate,  init_func = init,
                               frames = num_step+1, interval = 50, blit = True,repeat=False) 

# plt.title('be a-maze-d')

# saves the animation in local machine
# anim.save('growingCoil.mp4', writer = 'ffmpeg', fps = 30)

# Display the plot
plt.tight_layout()
plt.show(block=False)
plt.pause(1)
print(f"It took {run_count} runs to reach the goal within 500 random steps")
print('Press enter to close the plot')
input()
plt.close()


