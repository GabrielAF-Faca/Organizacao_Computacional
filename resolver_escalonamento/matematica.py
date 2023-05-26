

class Matematica:

    @staticmethod
    def printar_sistema(sistema):
        for i in sistema:
            print(i)

    @staticmethod
    def ajustar_diagonal(linha, pivot): # volta o valor da diagonal principal para 1

        if pivot != 0:
            linha = [round(valor / pivot, 3) for valor in linha]

        return linha

    @staticmethod
    def escalonar(sistema): # função para escalonar o sistema

        tam = len(sistema) # pega o tamanho do sistema

        for linha in range(tam):
            sistema[linha] = Matematica.ajustar_diagonal(sistema[linha], sistema[linha][linha])

        for linha in range(tam): # percorre cada linha

            pivot = sistema[linha][linha] # pivot é a diagonal principal dessa linha

            if pivot != 1: # se o pivot for diferente de 1

                sistema[linha] = Matematica.ajustar_diagonal(sistema[linha], pivot) # divide toda a linha pelo pivot

            for i in range(tam): # percorre cada linha de novo


                if i == linha: # se a linha atual for igual a linha anterior (diag) vai pra proxima iteracao
                    continue

                val = sistema[i][linha] # valores da coluna abaixo e acima da matriz principal

                for j in range(len(sistema[linha])): # percorre cada coluna da matriz

                    sistema[i][j] += -val * sistema[linha][j] # faz a formula do escalonamento em cada elemento

        sistema = [[round(coef, 3) for coef in linha] for linha in sistema] # arredonda todos os coefs do sistema

        return sistema # retorna o sistema
