'''
Exercício 1 - Aula #2
Programaê - Python
http://programae.org.br
'''
from turtle import *
setup(width=960, height=720, startx=0, starty=0)
title("Exercício 1 - Aula 2")
bgpic("ex1_papel_quadriculado.gif")

# define o "desenhista", substitua XXXXX pelo seu nome
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
professor.avance(140)
professor.esquerda(90)
professor.avance(140)
professor.esquerda(90)
professor.avance(140)
professor.esquerda(90)
professor.avance(140)
# FIM
professor.color("white")
professor.goto(-115, -92)
professor.color("black")
professor.write("Anyone Can Learn", None, None, "24pt bold")

# espera um clique do mouse pra sair
exitonclick()
