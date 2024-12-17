# -*- coding: utf-8 -*-

from tabuleiro import Tabuleiro
from typing import Tuple 


class Jogador:
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        self.matriz = tabuleiro.matriz
        self.tabuleiro = tabuleiro
        self.tipo = tipo
        
      
    def getJogada(self) -> Tuple[int, int]:
        pass
