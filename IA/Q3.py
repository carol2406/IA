import random

# Gerar 100 números aleatórios entre 0 e 1000
numeros = [random.randint(0, 1000) for _ in range(100)]

# Cálculo da média
media = sum(numeros) / len(numeros)

# Cálculo da variância
variancia = sum((x - media) ** 2 for x in numeros) / len(numeros)

# Cálculo do desvio padrão
desvio_padrao = variancia ** 0.5

print("\nQuestão 3:")
print(f"Média: {media}")
print(f"Variância: {variancia}")
print(f"Desvio padrão: {desvio_padrao}")
