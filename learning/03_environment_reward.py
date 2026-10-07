# 第三阶段：Environment + Reward
# 执行动作，并计算 Reward

state = {
    "A": 10,
    "B": 2
}

action = {
    "from": "A",
    "to": "B",
    "quantity": 3
}


def step(state, action):
    from_station = action["from"]
    to_station = action["to"]
    quantity = action["quantity"]

    # 执行调度
    state[from_station] -= quantity
    state[to_station] += quantity

    # 一个简单的 Reward
    reward = quantity * 2 - quantity * 1

    return state, reward


next_state, reward = step(state, action)

print("调度前状态：")
print({
    "A": 10,
    "B": 2
})

print("执行的 Action：")
print(action)

print("调度后状态：")
print(next_state)

print("Reward：")
print(reward)