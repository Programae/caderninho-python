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

'''
Mapeamento das regras

Dica: crie junto com seus alunos estas regras de movimentação.

____.avance(passos) -> avança com a tartaruga o número de passos especificado
____.recue(passos) -> recua com a tartura o número de passos especificado
____.direita(ângulo) -> vira pra "direta" o numero de graus especificado
____.esquerda(ângulo) -> vira pra "esquerda" o numero de graus especificado
'''

professor.avance = professor.forward
professor.recue = professor.back
professor.direita = professor.right
professor.esquerda = professor.left

# desenha um quadrado
professor.avance(100)
professor.direita(90)
professor.avance(100)
professor.esquerda(90)
professor.recue(100)
professor.direita(90)
professor.recue(100)

# espera um clique do mouse pra sair
exitonclick()
