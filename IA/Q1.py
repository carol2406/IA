# Questão 1
# Sequência numérica crescente de 0 a 20
numeros = list(range(0, 21))

# Média
media = sum(numeros) / len(numeros)

# Variância
variancia = sum((x - media) ** 2 for x in numeros) / len(numeros)

# Desvio padrão
desvio_padrao = variancia ** 0.5

print("Questão 1")
print(f"Média: {media}")
print(f"Variância: {variancia}")
print(f"Desvio padrão: {desvio_padrao}")