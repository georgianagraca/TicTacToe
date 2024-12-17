# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [ [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO], 
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]]
       
        
    def tem_campeao(self):
        for player in [Tabuleiro.JOGADOR_0, Tabuleiro.JOGADOR_X]:
            for i in range(3):
                if all(self.matriz[i][j] == player for j in range(3)) or all(self.matriz[j][i] == player for j in range(3)):
                    return player
            if all(self.matriz[i][i] == player for i in range(3)) or all(self.matriz[i][2-i] == player for i in range(3)):
                return player
        return Tabuleiro.DESCONHECIDO

    def verificaVitoria(self, tipo):
        return self.tem_campeao() == tipo