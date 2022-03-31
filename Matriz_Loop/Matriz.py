# Dirotrio criado para uma questão em que era necessário criar duas matrizes 3x3 e soma-las;
# Após somar era necessario printar cada linha somada, uma de cada vez, porém é possivel usar para qualquer tipo de
# matrizes de mesmas dimensões.

# facilitar a distribuição de valores
class Matriz:
    def __init__(self, colunas, linhas):
        # uma quantidade de colunas e linhhas que serão usadas em futaras ações
        self.colunas = colunas
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