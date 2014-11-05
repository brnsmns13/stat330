import random

row1 = [.64, .32, .04]
row2 = [.40, .50, .10]
row3 = [.25, .50, .25]

m1 = [row1, row2, row3]

state_counts = [0, 0, 0]

print m1

current_state = 0

def transition(state):
    r = round(random.random(), 2)
    transitions = m1[current_state] 
    cuml = 0
    for i, val in enumerate(transitions):
        cuml += val
        if r <= cuml:
            return i


for i in range(10000):
    current_state =  transition(current_state)
    state_counts[current_state] += 1

print state_counts

