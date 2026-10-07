# 第四阶段：尝试不同的 Action

def step(state, action):
    from_station = action["from"]
    to_station = action["to"]
    quantity = action["quantity"]

    state[from_station] -= quantity
    state[to_station] += quantity

    # B站希望保持5辆车
    target = 5

    shortage_before = max(
        target - (state[to_station] - quantity),
        0
    )

    shortage_after = max(
        target - state[to_station],
        0
    )

    reward = (shortage_before - shortage_after) * 10 - quantity

    return state, reward


print("尝试不同的调度数量：")

for quantity in range(1, 6):

    # 每次实验都从相同状态开始
    state = {
        "A": 10,
        "B": 2
    }

    action = {
        "from": "A",
        "to": "B",
        "quantity": quantity
    }

    next_state, reward = step(state, action)

    print(
        "调度",
        quantity,
        "辆：",
        "调度后状态 =",
        next_state,
        "Reward =",
        reward
    )