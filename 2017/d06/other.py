

def solve(input, i=0):
    state, states = [int(l) for l in input.split()], []
    while state not in states:
        states.append(state[:])
        mx, i = max(state), i+1
        mxi = state.index(mx)
        state[mxi] = 0
        while mx:
            mxi, mx = mxi+1, mx-1
            state[mxi % len(state)] += 1
    return i, i-states.index(state)

print solve(open('input').read())
