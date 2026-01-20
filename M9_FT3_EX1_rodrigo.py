"""
Solicitar ao utilizador uma palavra e apresentar todas as letras da palavra em
linhas separadas.
No final devolver a quantidade de “e’s” que a palavra contém.
"""

x=input("uma palavra: ")
y=x.count("e")
z= x.count("E")
c=y+z
print(f"a {x} tem {c} letras E ou e")
