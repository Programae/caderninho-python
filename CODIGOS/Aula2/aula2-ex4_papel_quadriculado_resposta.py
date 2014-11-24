'''
Exercício 4 - Aula #2
Programaê - Python
http://programae.org.br
'''
from turtle import *
setup(width=960, height=720, startx=0, starty=0)
title("Exercício 4 - Aula 2")
bgpic("ex4_papel_quadriculado.gif")
# substitua XXXXX pelo seu nome em todos os lugares que aparecer

# define o "desenhista"
professor = Turtle()
professor.pensize(5)

# personalizações: mostra o desenho da tartaruga
professor.shape("turtle")
professor.showturtle()

professor.avance = professor.forward
professor.recue = professor.back
professor.direita = professor.right
professor.esquerda = professor.left

# COLOQUE SEU CÓDIGO AQUI
professor.avance(285)
professor.esquerda(135)
professor.avance(150)
professor.esquerda(135)
professor.avance(215)
professor.esquerda(135)
professor.avance(150)

# FIM


# espera um clique do mouse pra sair
exitonclick()
