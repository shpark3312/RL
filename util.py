import numpy as np

class Agent:

    def __init__(self,start_loc, stochasticity):
        self.curr_loc = start_loc
        self.reward_tot = 0
        self.reward_hist=[]
        #print(self.curr_loc)
        self.path = []
        self.path.append(start_loc)
        self.stochasticity = stochasticity
        #print(self.path)

    # 에이전트의 위치,보상,경로를 초기 상태로 재설정
    def reset(self,start_loc):
        self.curr_loc = start_loc
        self.reward_tot = 0
        self.reward_hist=[]
        self.path = []
        self.path.append(start_loc)

    # 에이전트를 무작위 방향으로 이동시킴, 0-1 사이의 무작위 숫자를 생성하여 방향 결정
    def step_rand_dir(self):
        sample = np.random.random_sample()
        #print(sample)

        if sample <= 0.25:
            direction = 'up'
        elif 0.25 < sample <= 0.5:
            direction = 'left'
        elif 0.5 < sample <= 0.75:
            direction = 'down'
        elif 0.75 < sample <= 1:
            direction = 'right'

        #print(direction)
        direction = self.step_randomizer(direction)
        #print(direction)
        self.step(direction)
    # 주어진 방향으로 에이전트를 이동시키는 메서드. 벽이 있는 경우 에이전트는 이동하지 x
    def step(self,direction):

        if direction == 'up':
            update = self.curr_loc + [-1,0]
            # print(maze[[update[0]],[update[1]]])
            if maze[[update[0]],[update[1]]] == 1:
                self.curr_loc = self.curr_loc
                # print(self.curr_loc)
                # print(maze[[self.curr_loc[0]],[self.curr_loc[1]]])
                self.path.append(self.curr_loc)
                self.reward_check()
            else:
                self.curr_loc = update
                # print(self.curr_loc)
                # print(maze[[self.curr_loc[0]],[self.curr_loc[1]]])
                self.path.append(self.curr_loc)
                self.reward_check()

        elif direction == 'left':
            update = self.curr_loc + [0,-1]
            # print(maze[[update[0]],[update[1]]])
            if maze[[update[0]],[update[1]]] == 1:
                self.curr_loc = self.curr_loc
                # print(self.curr_loc)
                # print(maze[[self.curr_loc[0]],[self.curr_loc[1]]])
                self.path.append(self.curr_loc)
                self.reward_check()
            else:
                self.curr_loc = update
                # print(self.curr_loc)
                # print(maze[[self.curr_loc[0]],[self.curr_loc[1]]])
                self.path.append(self.curr_loc)
                self.reward_check()

        elif direction == 'down':
            update = self.curr_loc + [1,0]
            # print(maze[[update[0]],[update[1]]])
            if maze[[update[0]],[update[1]]] == 1:
                self.curr_loc = self.curr_loc
                # print(self.curr_loc)
                # print(maze[[self.curr_loc[0]],[self.curr_loc[1]]])
                self.path.append(self.curr_loc)
                self.reward_check()
            else:
                self.curr_loc = update
                # print(self.curr_loc)
                # print(maze[[self.curr_loc[0]],[self.curr_loc[1]]])
                self.path.append(self.curr_loc)
                self.reward_check()

        elif direction == 'right':
            update = self.curr_loc + [0,1]
            # print(maze[[update[0]],[update[1]]])
            if maze[[update[0]],[update[1]]] == 1:
                self.curr_loc = self.curr_loc
                # print(self.curr_loc)
                print(maze[[self.curr_loc[0]],[self.curr_loc[1]]])
                self.path.append(self.curr_loc)
                self.reward_check()
            else:
                self.curr_loc = update
                #print(self.curr_loc)
                print(maze[[self.curr_loc[0]],[self.curr_loc[1]]])
                self.path.append(self.curr_loc)
                self.reward_check()

        else:
            print("Invalid direction used")
    # 주어진 방향을 기준으로 무작위 방향을 결정함, 확률을 기반으로 무작위 이동확률 설정
    def step_randomizer(self,direction):

        random_param = 1 - self.stochasticity
        random_prob = np.random.random_sample()

        if random_prob > (1-random_param):
            return direction
        else:
            print("random step has occured")
            if direction == 'up':
                if random_prob <= ((1-random_param)/3):
                    direction = 'left'
                    return direction
                if ((1-random_param)/3) < random_prob <= (2*(1-random_param)/3):
                    direction = 'right'
                    return direction
                if (2*(1-random_param)/3) < random_prob <= (1-random_param):
                    direction = 'down'
                    return direction
            elif direction == 'left':
                if random_prob <= ((1-random_param)/3):
                    direction = 'up'
                    return direction
                if ((1-random_param)/3) < random_prob <= (2*(1-random_param)/3):
                    direction = 'right'
                    return direction
                if (2*(1-random_param)/3) < random_prob <= (1-random_param):
                    direction = 'down'
                    return direction
            elif direction == 'right':
                if random_prob <= ((1-random_param)/3):
                    direction = 'up'
                    return direction
                if ((1-random_param)/3) < random_prob <= (2*(1-random_param)/3):
                    direction = 'left'
                    return direction
                if (2*(1-random_param)/3) < random_prob <= (1-random_param):
                    direction = 'down'
                    return direction
            elif direction == 'down':
                if random_prob <= ((1-random_param)/3):
                    direction = 'up'
                    return direction
                if ((1-random_param)/3) < random_prob <= (2*(1-random_param)/3):
                    direction = 'right'
                    return direction
                if (2*(1-random_param)/3) < random_prob <= (1-random_param):
                    direction = 'left'
                    return direction
    # 에이전트의 현재 위치에 따라 보상을 확인하고 업데이트함
    def reward_check(self,*args):
        if (len(args) != 0):  self.curr_loc = args[0]

        action = -1
        oil = -5
        bump = -10
        goal = 200

        if maze[[self.curr_loc[0]],[self.curr_loc[1]]] == 2:
            self.reward_tot += bump
        if maze[[self.curr_loc[0]],[self.curr_loc[1]]] == 3:
            self.reward_tot += oil
        if maze[[self.curr_loc[0]],[self.curr_loc[1]]] == 5:
            self.reward_tot += goal
        self.reward_tot += action
        self.reward_hist.append(self.reward_tot)
        # print(self.reward_tot)
    # 주어진 스텝 수 만큼 무작위 방향으로 에이전트를 이동시킴
    def generate_rand_path(self,num_steps):
        for i in range(num_steps):
            self.step_rand_dir()

    def step_optimal_policy(self, optimal_policy):
        state = (self.curr_loc[0], self.curr_loc[1])
        action = optimal_policy[state]
        self.step(direction)

        # 'direction'을 사용하기 위해 액션을 문자열로 변환
        direction = None
        if action == (0, 1):
            direction = 'right'
        elif action == (1, 0):
            direction = 'down'
        elif action == (0, -1):
            direction = 'left'
        elif action == (-1, 0):
            direction = 'up'

p = 0.02
gamma = 0.95
theta = 0.01
start = np.array([15,4])
end = np.array([3,13])

# class MazeEnvironment:
#     def __init__(self, maze, start, end):
#         self.maze = maze
#         self.start = start
#         self.end = end
#         self.states = [(i, j) for i in range(maze.shape[0]) for j in range(maze.shape[1]) if maze[i, j] != -1]
#         self.actions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

#     def is_valid_state(self, state):
#         return 0 <= state[0] < self.maze.shape[0] and 0 <= state[1] < self.maze.shape[1] and self.maze[state[0], state[1]] != -1

#     def get_next_state(self, state, action):
#         next_state = (state[0] + action[0], state[1] + action[1])
#         if self.is_valid_state(next_state):
#             return next_state
#         else:
#             return state

#     def get_transition_probability(self, state, action, next_state):
#         intended_next_state = self.get_next_state(state, action)
#         if intended_next_state == next_state:
#             return 1
#         elif intended_next_state == state and next_state == state:
#             return 1 - sum(self.get_transition_probability(state, a, self.get_next_state(state, a)) for a in self.actions)
#         else:
#             return 0

#     def get_reward(self, state, action, next_state):
#         if next_state == self.end:
#             return 200
#         elif state == next_state:
#             return -1
#         else:
#             return -1

# import random

# class Agentpolicy:
#     def __init__(self, env):
#         self.env = env
#         self.policy = {state: random.choice(env.actions) for state in env.states}
#         self.gamma = 0.95

#     def policy_iteration(self, theta=0.01):
#         while True:
#             V = self.policy_evaluation(self.policy, theta)
#             new_policy = self.policy_improvement(V)
#             if new_policy == self.policy:
#                 break
#             else:
#                 self.policy = new_policy
#         return self.policy
    
#     def policy_evaluation(self, policy, theta=0.01):
#         V = {state: 0 for state in self.env.states}
#         while True:
#             delta = 0
#             for state in self.env.states:
#                 v = V[state]
#                 V[state] = sum(self.env.get_transition_probability(state, policy[state], next_state) * (self.env.get_reward(state, policy[state], next_state) + self.gamma * V[next_state]) for next_state in self.env.states)
#                 delta = max(delta, abs(v - V[state]))
#             if delta < theta:
#                 break
#         return V

#     def policy_improvement(self, V):
#         new_policy = {state: None for state in self.env.states}
#         for state in self.env.states:
#             action_values = [sum(self.env.get_transition_probability(state, action, next_state) * (self.env.get_reward(state, action, next_state) + self.gamma * V[next_state]) for next_state in self.env.states) for action in self.env.actions]
#             new_policy[state] = self.env.actions[np.argmax(action_values)]
#         return


maze = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 2, 2, 0, 1, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 1],
    [1, 0, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 2, 0, 1, 0, 0, 3, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 2, 0, 1],
    [1, 0, 2, 1, 0, 0, 1, 0, 0, 1, 2, 2, 1, 1, 1, 1, 0, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 3, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 2, 2, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 2, 2, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 3, 0, 0, 1, 1, 1, 1, 2, 2, 1],
    [1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 3, 0, 0, 3, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])
# # 1. Agentpolicy 인스턴스를 생성하고 policy_iteration 메서드를 호출하여 최적의 정책을 찾습니다.
# env = MazeEnvironment(maze, start, end)
# print(env)

# agent = Agentpolicy(env)
# optimal_policy = agent.policy_iteration()

# # 에이전트를 생성하고 시작 위치로 초기화합니다.
# agent = Agent(start_loc=start, stochasticity=0.1)

# # 2. 에이전트가 최적의 정책에 따라 움직이도록 Agent 클래스의 step_optimal_policy 메서드를 호출합니다.
# while agent.curr_loc.tolist() != end.tolist():
#     agent.step_optimal_policy(optimal_policy)

# # 에이전트의 경로를 출력합니다.
# print("Agent's path:", agent.path)


