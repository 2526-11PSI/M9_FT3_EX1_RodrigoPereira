"""
d) Pedir duas palavras ao utilizador e apresentar no ecrã a palavra com mais
letras.
"""
x=input("insira uma palavra: ")
z=input("insira uma palavra: ")

if len(x)>len(z)  :
    print(f"{x} tem mais letras {z}")
elif len(x)<len(z):
    print(f"{z} tem mais letras {x}")
else:
    print("tenhem a mesma quantidade de letras ")  