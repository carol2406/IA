# Questão 2
# Sequência numérica qualquer
numeros = [5, 12, 8, 20, 15]  # Exemplo de sequência qualquer

# Média
media = sum(numeros) / len(numeros)

# Variância
variancia = sum((x - media) ** 2 for x in numeros) / len(numeros)

# Desvio padrão
desvio_padrao = variancia ** 0.5

print("\nQuestão 2")
print(f"Média: {media}")
print(f"Variância: {variancia}")
print(f"Desvio padrão: {desvio_padrao}")