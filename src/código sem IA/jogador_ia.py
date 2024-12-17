# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro
from typing import Tuple 


class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)
            

    def getJogada(self) -> Tuple[int, int]:
        def check_two_in_a_row(player):
            for i in range(3):
                if self.matriz[i].count(player) == 2 and Tabuleiro.DESCONHECIDO in self.matriz[i]:
                    return (i, self.matriz[i].index(Tabuleiro.DESCONHECIDO))
                col = [self.matriz[j][i] for j in range(3)]
                if col.count(player) == 2 and Tabuleiro.DESCONHECIDO in col:
                    return (col.index(Tabuleiro.DESCONHECIDO), i)
            diag1 = [self.matriz[i][i] for i in range(3)]
            if diag1.count(player) == 2 and Tabuleiro.DESCONHECIDO in diag1:
                idx = diag1.index(Tabuleiro.DESCONHECIDO)
                return (idx, idx)
            diag2 = [self.matriz[i][2-i] for i in range(3)]
            if diag2.count(player) == 2 and Tabuleiro.DESCONHECIDO in diag2:
                idx = diag2.index(Tabuleiro.DESCONHECIDO)
                return (idx, 2-idx)
            return None

        # R1
        move = check_two_in_a_row(self.tipo)
        if move:
            return move
        move = check_two_in_a_row(Tabuleiro.JOGADOR_X if self.tipo == Tabuleiro.JOGADOR_0 else Tabuleiro.JOGADOR_0)
        if move:
            return move

        # R2
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    self.matriz[l][c] = self.tipo
                    winning_moves = 0

                    for l2 in range(3):
                        for c2 in range(3):
                            if self.matriz[l2][c2] == Tabuleiro.DESCONHECIDO:
                                self.matriz[l2][c2] = self.tipo
                                if self.tabuleiro.verificaVitoria(self.tipo):
                                    winning_moves += 1
                                self.matriz[l2][c2] = Tabuleiro.DESCONHECIDO

                    self.matriz[l][c] = Tabuleiro.DESCONHECIDO

                    if winning_moves >= 2:
                        return (l, c)
                    
        # R3
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)

        # R4
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for corner in corners:
            opp_corner = (2-corner[0], 2-corner[1])
            if self.matriz[corner[0]][corner[1]] == (Tabuleiro.JOGADOR_X if self.tipo == Tabuleiro.JOGADOR_0 else Tabuleiro.JOGADOR_0) and self.matriz[opp_corner[0]][opp_corner[1]] == Tabuleiro.DESCONHECIDO:
                return opp_corner

        # R5
        for corner in corners:
            if self.matriz[corner[0]][corner[1]] == Tabuleiro.DESCONHECIDO:
                return corner

        # R6
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    return (l, c)

        return None