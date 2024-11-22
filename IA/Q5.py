# Sequências x e y quaisquer (exemplo)
x = [2, 4, 6, 8, 10]
y = [1, 3, 5, 7, 9]

# Número de elementos
n = len(x)

# Soma dos produtos cruzados, quadrados e totais
soma_x = sum(x)
soma_y = sum(y)
soma_xy = sum(x[i] * y[i] for i in range(n))
soma_x2 = sum(xi ** 2 for xi in x)
soma_y2 = sum(yi ** 2 for yi in y)

# Fórmula da correlação linear
correlacao = (n * soma_xy - soma_x * soma_y) / (
    ((n * soma_x2 - soma_x**2) * (n * soma_y2 - soma_y**2)) ** 0.5
)

print("\nQuestão 5:")
print(f"Correlação linear: {correlacao}")
