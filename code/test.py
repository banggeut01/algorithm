stick = ['B', 'Y', 'RR']

def makeStick(n):
    if n == 1: return 2
    if n == 2: return 5
    return makeStick(n - 1) * 2 + makeStick(n - 2)

print(makeStick(5))