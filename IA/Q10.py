import math
import random

# Funções de ativação
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Função para treinar a rede neural
def treinar_mlp(X, y, epochs=10000, lr=0.1):
    # Inicializar pesos e bias aleatórios
    random.seed(42)
    
    # X: Entradas (A, B), y: Saída esperada
    # Camada de entrada tem 2 neurônios (A e B)
    # Camada oculta tem 2 neurônios
    # Camada de saída tem 1 neurônio
    
    input_layer_size = 2  # A e B
    hidden_layer_size = 2
    output_layer_size = 1
    
    # Pesos aleatórios entre a camada de entrada e a camada oculta
    W1 = [[random.uniform(-1, 1) for _ in range(hidden_layer_size)] for _ in range(input_layer_size)]
    b1 = [random.uniform(-1, 1) for _ in range(hidden_layer_size)]
    
    # Pesos aleatórios entre a camada oculta e a camada de saída
    W2 = [[random.uniform(-1, 1) for _ in range(output_layer_size)] for _ in range(hidden_layer_size)]
    b2 = [random.uniform(-1, 1) for _ in range(output_layer_size)]
    
    # Treinamento
    for epoch in range(epochs):
        for i in range(len(X)):
            # Passagem pela rede (forward pass)
            
            # Camada oculta
            z1 = [sum(X[i][k] * W1[k][j] for k in range(input_layer_size)) + b1[j] for j in range(hidden_layer_size)]
            a1 = [sigmoid(z) for z in z1]
            
            # Camada de saída
            z2 = [sum(a1[k] * W2[k][j] for k in range(hidden_layer_size)) + b2[j] for j in range(output_layer_size)]
            a2 = [sigmoid(z) for z in z2]
            
            # Cálculo do erro (erro de saída)
            erro = [y[i][j] - a2[j] for j in range(output_layer_size)]
            
            # Backpropagation
            # Gradiente da camada de saída
            d2 = [erro[j] * sigmoid_derivative(a2[j]) for j in range(output_layer_size)]
            
            # Gradiente da camada oculta
            d1 = [sum(d2[k] * W2[j][k] for k in range(output_layer_size)) * sigmoid_derivative(a1[j]) for j in range(hidden_layer_size)]
            
            # Ajuste dos pesos e viéses
            for j in range(output_layer_size):
                for k in range(hidden_layer_size):
                    W2[k][j] += a1[k] * d2[j] * lr
                b2[j] += d2[j] * lr
            
            for j in range(hidden_layer_size):
                for k in range(input_layer_size):
                    W1[k][j] += X[i][k] * d1[j] * lr
                b1[j] += d1[j] * lr
        
        if epoch % 1000 == 0:
            erro_medio = sum(abs(e) for e in erro) / output_layer_size
            print(f'Época {epoch} - Erro Médio: {erro_medio}')
    
    return W1, b1, W2, b2, a2

# Dados de entrada e saída esperada
X = [[0, 0],
     [0, 1],
     [1, 0],
     [1, 1]]

y = [[1],
     [0],
     [0],
     [1]]

# Treinar a rede neural
W1, b1, W2, b2, a2 = treinar_mlp(X, y, epochs=10000, lr=0.1)

# Exibir a saída final após o treinamento
print("\nSaída final após treinamento:")
print(a2)
