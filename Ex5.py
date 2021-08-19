valor = input("Digite um valor qualquer, pode ser número ou letra: ")

print("É número inteiro? ",isinstance(valor, int))
print("É número com virgula? ",isinstance(valor, float))
print("É letra com numero? ",isinstance(valor, bool))
print("É só letra? ",isinstance(valor, str))