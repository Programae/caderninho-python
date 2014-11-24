'''
Exemplo Aula #2
Programaê - Python
http://programae.org.br
'''
from turtle import *

# define o "desenhista"
professor = Turtle()
bgpic("plano_cartesiano.gif")

# personalizações: mostra o desenho da tartaruga
professor.shape("turtle")
professor.showturtle()
professor.pensize(5) # ajustando a espessura da linha

professor.avance = professor.forward
professor.recue = professor.back
professor.direita = professor.right
professor.esquerda = professor.left

# desenha um triângulo
professor.avance(100)
professor.direita(60)
professor.recue(100)
professor.direita(60)
professor.avance(100)

# espera um clique do mouse pra sair
exitonclick()
