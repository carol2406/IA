import random

# Função de ativação: função degrau
def step_function(x):
    return 1 if x >= 0 else 0

# Função para treinar o Perceptron
def treinar_perceptron(X, y, epochs=100, lr=0.1):
    # Inicializar pesos e viés com valores aleatórios
    random.seed(42)
    
    # X: Entradas (A, B), y: Saída esperada
    # Camada de entrada tem 2 neurônios (A e B)
    input_layer_size = 2  # A e B
    output_layer_size = 1  # Saída binária

    # Inicializar pesos e viéses aleatórios
    pesos = [random.random() for _ in range(input_layer_size)]
    vies = random.random()

    # Treinamento
    for epoch in range(epochs):
        erro_total = 0
        for i in range(len(X)):
            # Calcular soma ponderada (função soma)
            soma = sum(x * peso for x, peso in zip(X[i], pesos)) + vies
            
            # Aplicar função de ativação (função degrau)
            y_pred = step_function(soma)
            
            # Calcular erro (diferença entre a saída desejada e a previsão)
            erro = y[i] - y_pred
            erro_total += abs(erro)
            
            # Atualizar pesos e viéses com base no erro
            for j in range(len(pesos)):
                pesos[j] += lr * erro * X[i][j]
            vies += lr * erro

        # Exibir o erro médio a cada 1000 épocas
        if epoch % 1000 == 0:
            erro_medio = erro_total / len(X)
            print(f'Época {epoch} - Erro Médio: {erro_medio}')
    
    return pesos, vies

# Dados de entrada e saída esperada
X = [[0, 0],
     [0, 1],
     [1, 0],
     [1, 1]]

y = [0, 1, 1, 1]  # Saídas esperadas

# Treinar o Perceptron
pesos, vies = treinar_perceptron(X, y, epochs=10000, lr=0.1)

# Testar a rede neural com os dados de entrada
print("\nSaídas após treinamento:")
for x in X:
    soma = sum(x_i * peso for x_i, peso in zip(x, pesos)) + vies
    y_pred = step_function(soma)
    print(f"Entrada: {x} -> Saída prevista: {y_pred}")
