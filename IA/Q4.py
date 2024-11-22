x = [2, 3, 4, 5, 6]
y = [1, 2, 3, -3, 4]
n = len(x)

soma_x = sum(x)
soma_y = sum(y)
soma_xy = sum(x[i] * y[i] for i in range(n))
soma_x2 = sum(xi ** 2 for xi in x)
soma_y2 = sum(yi ** 2 for yi in y)

correlacao = (n * soma_xy - soma_x * soma_y) / (
    ((n * soma_x2 - soma_x*2) * (n * soma_y2 - soma_y2)) * 0.5
)

print(f"Correlação linear: {correlacao}")
