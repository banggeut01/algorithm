# test2.py
def test():
    global j
    if j == 2:
        j = 5

for i in range(10):
    for j in range(10):
        test()
        print(i, j)
