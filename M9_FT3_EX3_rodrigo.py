"""
Receber uma palavra e indicar o número de vezes que aparece a letra ‘a’.
Exemplo:
Palavra: caixa
2 ocorrências da letra ‘a’
"""

palavra=input("insira uma palavra")

a=palavra.count("a")
b=palavra.count("A")
c=a+b

print(f"A palavra{palavra} tem {c} a")