# -*- coding: utf-8 -*-
"""Python para FUTEBOL_01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zThigkqMaqhdPGvhZZBxaBuVnobIcr6A

Importando Biblioteca
"""

import pandas as pd

"""Extraíndo e Armazenando o Banco de Dados

https://www.football-data.co.uk/
"""

df = pd.read_csv("https://www.football-data.co.uk/mmz4281/2021/E0.csv")
#df = pd.read_csv("E0.csv")

"""(Lendo) Exibindo em tela o BD"""

display(df)
# print(df)
# df

"""Selecionando Colunas de Interesse"""

df = df [["Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR", "B365H", "B365D", "B365A"]]
display(df)

"""Salvando dados selecionados em arquivo .xlsx para Download"""

df.to_excel("PremierLeague.xlsx")