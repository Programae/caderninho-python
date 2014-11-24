'''
Exercício 1 - Aula #2
Programaê - Python
http://programae.org.br
'''
from turtle import *

setup(width=960, height=720, startx=0, starty=0)

# define o "desenhista", substitua XXXXX pelo seu nome
XXXXX = Turtle()
bgpic("ex1_papel_quadriculado.gif")
XXXXX.pensize(5)

# personalizações: mostra o desenho da tartaruga
XXXXX.shape("turtle")
XXXXX.showturtle()

XXXXX.avance = XXXXX.forward
XXXXX.recue = XXXXX.back
XXXXX.direita = XXXXX.right
XXXXX.esquerda = XXXXX.left

# COLOQUE SEU CÓDIGO AQUI


# FIM


# espera um clique do mouse pra sair
exitonclick()
