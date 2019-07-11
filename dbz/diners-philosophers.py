# Dining Philosophers
#
# Set up: 5 Philosophers sitting at a table
#         Each has bowl
#         5 Chopsticks
# Rule 1: Philosopher can only pick up one stick at a time.
# Rule 2: Philosopher holds chopstick until done eating.
# Rule 3: Need two chopsticks to eat.
# Rule 4: Put both chopsticks down when done eating.
# Rule 5: Only one move is made a time (by any philosopher)
# Question: Will all philosophers eat? (eventually)
init = (
    ['Hungry'] * 5,
    ['None'] * 5
)

def next_state(state, i):
    # Return possible state for philosopher i
    if state[0][i] == 'Hungry' and state[1][i] == None:
        new_state = (
            state[0],
            list(state[1]))
        new_state[1][i] = i # take possession
        return new_state
    if state[0][i] == 'Hungry' and state[1][i] and state[1][(i+1)%5] == i:
        # State 1: Hungry, holding left chopstick, right chopstick is available
        # Grab it.
        new_state = (
            list(state[0]),
            list(state[1]) # make copy
        )
        new_state[0][i] = 'Eaten'
        new_state[l][i] = None
        new_state[1][(i + 1) % 5] = None
        return new_state
    return None

must_check = [ init ]
while must_check:
    state = must_check.pop(0)
    before = len(must_check)
    for i in range(5):
        ns = next_state(state, i)
        if ns:
            must_check.append(ns)
    after = len(must_check)
    if before == after and not all(s == 'Eaten' for s in state[0]):
        print("DeadLock in state", state)
