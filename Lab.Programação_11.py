# facilitar a distribuição de valores
class Matriz:
    def __init__(self, colunas, linhas):
        self.colunas = colunas  # uma quantidade de colunas que será usada em futaras ações
        self.linhas = linhas

    def cria_matriz_loop(self):
        """
        Uma função em uma classe que cria uma matriz a partir do modelo matriz que deseja ser criada
        atravez de um loop.
        :return: Retorna a matriz
        """
        matriz = []
        for l in range(self.linhas):
            linhas = []

            for c in range(self.colunas):
                numero = int(input())
                linhas.append(numero)

            matriz.append(linhas)

        return matriz

    def soma_matriz_iguais_loop(self, matriz_1, matriz_2):
        """
        Uma função em uma classe que soma duas matrizes iguais ao modelo que deseja atravez de um loop.
        OBS : É necessario ter um modelo padrão para somar.
        :param matriz_1: Matriz de n dimensoes.
        :param matriz_2: Matriz de n dimensoes.
        :return: a soma de duas matrizes
        """
        matriz_somada = []
        for l in range(self.linhas):
            # soma de cada dimensao
            sum_colunas = []

            for c in range(self.colunas):
                # percorre e soma cada valor de ambas matrizes e printa cada axe
                c1 = matriz_1[l][c]
                c2 = matriz_2[l][c]
                sum_c = c1 + c2
                sum_colunas.append(sum_c)

            matriz_somada.append(sum_colunas)

        return matriz_somada


matriz_formato = Matriz(3, 3)
matriz_1 = matriz_formato.cria_matriz_loop()
matriz_2 = matriz_formato.cria_matriz_loop()
matriz_somada = matriz_formato.soma_matriz_iguais_loop(matriz_1, matriz_2)
print(matriz_1)
print(matriz_2)
for m in matriz_somada:
    print(m)
