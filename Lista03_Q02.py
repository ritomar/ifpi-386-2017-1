# 2. Faça um programa que leia um nome de usuário e a sua senha e não
#    aceite a senha igual ao nome do usuário, mostrando uma mensagem
#    de erro e voltando a pedir as informações.


nome = input("Digite o nome: ")
senha = input("Digite a senha: ")
while nome == senha:
    print("Senha inválida.")
    senha = input("Digite a senha: ")

print("Nome e senha informados com sucesso.")

