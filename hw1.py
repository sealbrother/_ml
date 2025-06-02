import random
def hillClimbing(x, height, neighbor, max_fail=10000):
    fail = 0
    while True:
        nx = neighbor(x)
        if height(nx) > height(x):
            x = nx
            fail = 0
        else:
            fail += 1
            if fail > max_fail:
                return x
def neighbor(x, h=0.01):
    return [xi + random.uniform(-h, h) for xi in x]

def height(x):
    return -(x[0]**2 + x[1]**2 + x[2]**2 - 2*x[0] - 4*x[1] - 6*x[2] + 8)
x = hillClimbing([0, 0, 0], height, neighbor)
f_val = x[0]**2 + x[1]**2 + x[2]**2 - 2*x[0] - 4*x[1] - 6*x[2] + 8
print("x = {:.3f}, y = {:.3f}, z = {:.3f}, f(x, y, z) = {:.3f}".format(x[0], x[1], x[2], f_val))
