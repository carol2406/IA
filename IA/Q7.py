import heapq

# Grafo com custos das rotas (baseado na imagem)
grafo = {
    "Cuiabá": {"Brasília": 1137, "Campo Grande": 694},
    "Brasília": {"Belo Horizonte": 740, "São Paulo": 1015},
    "Campo Grande": {"São Paulo": 1014, "Curitiba": 991},
    "Belo Horizonte": {"Rio de Janeiro": 434, "São Paulo": 586},
    "São Paulo": {"Curitiba": 408},
    "Rio de Janeiro": {"Curitiba": 843},
    "Curitiba": {"Florianópolis": 300},
}

# Função do Algoritmo A*
def algoritmo_a_estrela(grafo, inicio, objetivo, heuristica):
    fila = []
    heapq.heappush(fila, (0, inicio))
    custos = {inicio: 0}
    caminho = {}

    while fila:
        custo_atual, atual = heapq.heappop(fila)

        if atual == objetivo:
            rota = []
            while atual in caminho:
                rota.append(atual)
                atual = caminho[atual]
            rota.append(inicio)
            return rota[::-1], custos[objetivo]

        for vizinho, peso in grafo[atual].items():
            novo_custo = custos[atual] + peso
            if vizinho not in custos or novo_custo < custos[vizinho]:
                custos[vizinho] = novo_custo
                prioridade = novo_custo + heuristica.get(vizinho, 0)
                heapq.heappush(fila, (prioridade, vizinho))
                caminho[vizinho] = atual

    return None, float("inf")


# Heurística estimada (distância em linha reta para Florianópolis)
heuristica = {
    "Cuiabá": 2000,
    "Brasília": 1700,
    "Campo Grande": 1300,
    "Belo Horizonte": 1600,
    "São Paulo": 500,
    "Rio de Janeiro": 800,
    "Curitiba": 300,
    "Florianópolis": 0,
}

# Executando o algoritmo para Cuiabá -> Florianópolis
rota, custo = algoritmo_a_estrela(grafo, "Cuiabá", "Florianópolis", heuristica)
print("Questão 7:")
print(f"Rota: {' -> '.join(rota)}")
print(f"Custo total: {custo}")
