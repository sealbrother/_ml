from micrograd.engine import Value

x = Value(0.0)
y = Value(0.0)
z = Value(0.0)

params = [x, y, z]
step = 0.1

for i in range(5000):
    for p in params:
        p.grad = 0

    loss = x**2 + y**2 + z**2 - 2*x - 4*y - 6*z + 8
    loss.backward()

    if i % 1000 == 0 and i > 0:
        step *= 0.5  

    for p in params:
        p.data -= step * p.grad

print(f'x={x.data:.6f} y={y.data:.6f} z={z.data:.6f}')