from gym.envs.registration import register

register(
    id='modified_InvertedDoublePendulum-v0',
    entry_point='gym_modified_InvertedDoublePendulum_v2.envs:ModifiedInvertedDoublePendulumEnv',
)
