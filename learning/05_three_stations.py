# 第五阶段：三站共享单车调度

def step(state, action):
    from_station = action["from"]
    to_station = action["to"]
    quantity = action["quantity"]

    # 执行调度
    state[from_station] -= quantity
    state[to_station] += quantity

    # 每个站点希望保持的车辆数量
    target = 5

    # 调度前的缺车数量
    shortage_before = max(
        target - (state[to_station] - quantity),
        0
    )

    # 调度后的缺车数量
    shortage_after = max(
        target - state[to_station],
        0
    )

    # Reward
    reward = (shortage_before - shortage_after) * 10 - quantity

    return state, reward


def choose_best_action(state):
    best_action = None
    best_reward = float("-inf")

    stations = list(state.keys())

    # 尝试所有起点和终点
    for from_station in stations:
        for to_station in stations:

            if from_station == to_station:
                continue

            # 尝试调度1～3辆
            for quantity in range(1, 4):

                test_state = state.copy()

                # 车辆不够时跳过
                if test_state[from_station] < quantity:
                    continue

                action = {
                    "from": from_station,
                    "to": to_station,
                    "quantity": quantity
                }

                next_state, reward = step(
                    test_state,
                    action
                )

                print(
                    from_station,
                    "→",
                    to_station,
                    quantity,
                    "辆",
                    "Reward =",
                    reward
                )

                if reward > best_reward:
                    best_reward = reward
                    best_action = action

    return best_action, best_reward


# 当前共享单车状态
state = {
    "A": 10,
    "B": 2,
    "C": 7
}

print("当前状态：")
print(state)

print("\n开始寻找最佳动作：")

best_action, best_reward = choose_best_action(state)

print("\n最佳 Action：")
print(best_action)

print("最高 Reward：")
print(best_reward)