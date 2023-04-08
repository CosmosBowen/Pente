tree = {
    "O": ("A", "B", "C"),
    "A": ("A1", "A2", "A3"),
    "B": ("B1", "B2", "B3"),
    "C": ("C1", "C2", "C3", "C4"),
    "A1": ("A11", "A12"),
    "A2": ("A21", "A22", "A23"),
    "A3": ("A31", "A32", "A33", "A34"),
    "B1": ("B11", "B12"),
    "B2": ("B21", "B22", "B23"),
    "B3": ("B31", "B32", "B33", "B34"),
    "C1": ("C11", "C12"),
    "C2": ("C21", "C22", "C23"),
    "C3": ("C31"),
    "C4": ("C41", "C42", "C43")
}

evaluation = {
    "A11": 3,
    "A12": 5,

    "A21": 1,
    "A22": 5,
    "A23": 7,

    "A31": 3,
    "A32": 8,
    "A33": 2,
    "A34": 5,

    "B11": 7,
    "B12": 6,

    "B21": 2,
    "B22": 9,
    "B23": 4,

    "B31": 3,
    "B32": 8,
    "B33": 7,
    "B43": 4,

    "C11": 4,
    "C12": 3,

    "C21": 5,
    "C22": 6,
    "C23": 9,

    "C31": 4,

    "C41": 9,
    "C42": 8,
    "C43": 9,
}

player = 1
opponent = 2


def Evaluation(state):
    return evaluation[state]


def Actions(state):
    actions = []
    next_states = tree[state]
    for next_state in next_states:
        actions.append((state, next_state))
    # print("actions:", actions)
    return actions


def Next_State(state, action):
    if state == action[0]:
        return action[1]


def Alpha_Beta_Pruning(state, depth):
    print("DEPTH(Alpha_Beta_Pruning):", depth)
    value, move = Max_Value(state, float('-inf'), float('inf'), depth)
    return value, move


def Max_Value(state, alpha, beta, depth):
    print("DEPTH(Max_Value):", depth)
    if depth == 0:
        res = Evaluation(state)
        print("Max_Evaluation:", state, ":", res)
        return res
        # return Evaluation(state)
    v = float('-inf')
    best_action = None
    actions = Actions(state)
    for action in actions:
        print("\nMax_action:", action)
        next_state = Next_State(state, action)
        print("Max_next_state:", next_state)
        move = action
        value = 0
        res = Min_Value(next_state, alpha, beta, depth-1)
        print(state, ":", action, "get Min_Value:", res)
        try:
            value = res[0]
            move = res[1]
        except TypeError:
            value = res
            # pass
        finally:
            # print("value:", value, " move:", move)
            if value > v:
                v = value
                best_action = action
            if v >= beta:
                print("return:", v, ">=", beta)
                return v, action
            alpha = max(v, alpha)
    return v, best_action


def Min_Value(state, alpha, beta, depth):
    print("DEPTH(Min_Value):", depth)
    if depth == 0:
        res = Evaluation(state)
        print("Min_Evaluation:", state, ":", res)
        return res
        # return Evaluation(state)
        # return Evaluation(state, opponent)
    # if is_End(state):
    #     return Evaluation(state, opponent)
    v = float('inf')
    best_action = None
    actions = Actions(state)
    for action in actions:
        print("\nMin_action:", action)
        next_state = Next_State(state, action)
        print("Min_next_state:", next_state)
        move = action
        value = 0
        res = Max_Value(next_state, alpha, beta, depth-1)
        print(state, ":", action, "get Max_Value:", res)
        try:
            value = res[0]
            move = res[1]
        except TypeError:
            value = res
            # pass
        finally:
            # print("value:", value, " move:", move)
            if value < v:
                v = value
                best_action = action
            if v <= alpha:
                print("return:", v, "<=", alpha)
                return v, action
            beta = min(v, beta)
    return v, best_action


state = "O"
res = Alpha_Beta_Pruning(state, depth=3)
print(res)
