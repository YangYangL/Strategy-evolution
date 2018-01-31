import gym
from DQN_class import *

# ENV_NAME ='Reated_Envolver'
ENV_NAME = 'CartPole-v0'
EPISODE = 10000
STEP = 300
TEST = 10


def main():
    env = gym.make(ENV_NAME)
    agent = DQN(env)

    for episode in range(EPISODE):
        # initialize task
        state = env.reset()
        # Train
        for step in range(STEP):
            action = agent.egreedy_action(state)
            next_state, reward, done, _ = env.step(action)
            # define reward for agent
            # reward_agent = -1 if done else 0.1
            agent.perceive(state, action, reward, next_state, done)
            state = next_state
            if done:
                break

    # Test every 100 episodes

    if episode % 100 == 0:
        total_reward = 0
        for i in range(TEST):
            state = env.render()
            for j in range(STEP):
                env.render()
                action = agent.acion(state)
                state, reward, done, _ = env.step(action)
                total_reward += reward
                if done:
                    break

            ave_reward = total_reward/TEST
            print('episode:', episode,'Evaluation Average Reward:', ave_reward)
            if ave_reward>=200:
                break


# if __name__ == '__main__ ':
#     main()

main()
