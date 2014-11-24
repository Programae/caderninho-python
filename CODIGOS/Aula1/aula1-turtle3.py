'''
Exemplo Aula #1
Programaê - Python
http://programae.org.br
'''
from turtle import *

# define o "desenhista"
professor = Turtle()

# personalizações: mostra o desenho da tartaruga
professor.shape("turtle")
professor.showturtle()

professor.avance = professor.forward
professor.recue = professor.back
professor.direita = professor.right
professor.esquerda = professor.left

# desenha um círculo
professor.circle(100) # raio 100

# espera um clique do mouse pra sair
exitonclick()
