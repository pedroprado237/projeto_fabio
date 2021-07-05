'''

Faça um algoritmo que leia o nome e a nota de 10 candidatas de um concurso.
Calcule e apresente a maior
nota e o nome da primeira colocada, sendo que não houve empate.

'''

cont = 0
maior_nota = 0


while cont < 10:
    nome = str (input("\nNome:"))
    nota = float (input("Nota:"))

    if maior_nota < nota:
        maior_nota = nota
        nome_maior = nome
      
    cont = cont +1

print ("\nCandidata:",nome_maior,",maior nota:",maior_nota,)
