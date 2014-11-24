'''
Exemplo Aula #1
Programaê - Python
http://programae.org.br
'''
from turtle import *

setup(width=960, height=720, startx=0, starty=0)

# define o "desenhista"
professor = Turtle()
bgpic("papel_quadriculado.gif")
professor.pensize(5)

# personalizações: mostra o desenho da tartaruga
professor.shape("turtle")
professor.showturtle()

professor.avance = professor.forward
professor.recue = professor.back
professor.direita = professor.right
professor.esquerda = professor.left

# desenha um círculo
professor.avance(100) # anda 100 passos
professor.direita(90) # vira 90 graus à direita
professor.avance(100) # anda 100 passos
professor.esquerda(90) # vira 90 graus a esquerda
professor.avance(100) # anda 100 passos
professor.esquerda(90) # vira 90 graus a esquerda
professor.avance(200) # anda 100 passos
professor.esquerda(90) # vira 90 graus a esquerda
professor.avance(415)
professor.esquerda(90) # vira 90 graus a esquerda
professor.avance(40)
# espera um clique do mouse pra sair
exitonclick()
