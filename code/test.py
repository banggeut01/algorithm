def b(array):
    array[0] = 100

def a():
    array = [1, 2, 3]
    print(array)
    b(array)
    print(array)

a()